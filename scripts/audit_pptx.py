"""Read-only checks for explicit academic presentation formatting, not visual QA."""
import argparse
import json
import re
import zipfile
import xml.etree.ElementTree as ET

NS = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}

def audit(path, chinese='Microsoft YaHei', latin='Arial'):
    errors, review = [], []
    slides = tables = charts = 0
    with zipfile.ZipFile(path) as package:
        for name in package.namelist():
            is_slide = bool(re.fullmatch(r'ppt/slides/slide\d+\.xml', name))
            is_chart = bool(re.search(r'/charts/chart\d+\.xml$', name))
            if not (is_slide or is_chart):
                continue
            root = ET.fromstring(package.read(name))
            if is_slide:
                slides += 1
            if is_chart:
                charts += 1
            for run in root.findall('.//a:r', NS):
                txt = run.findtext('a:t', '', NS)
                pr = run.find('a:rPr', NS)
                if pr is None:
                    continue  # inherited fonts require application inspection
                for has_script, tag, expected in [
                    (bool(re.search(r'[\u4e00-\u9fff]', txt)), 'ea', chinese),
                    (bool(re.search(r'[A-Za-z0-9]', txt)), 'latin', latin),
                ]:
                    explicit = pr.find('a:' + tag, NS)
                    if has_script and explicit is not None:
                        actual = explicit.get('typeface', '')
                        if actual and actual != expected:
                            errors.append(f'{name}: explicit {tag} font {actual!r}; expected {expected!r}')
            for table in root.findall('.//a:tbl', NS):
                tables += 1
                for index, cell in enumerate(table.findall('.//a:tc', NS), 1):
                    pr = cell.find('a:tcPr', NS)
                    if pr is None or pr.get('anchor') != 'ctr':
                        errors.append(f'{name}: table {tables} cell {index} lacks explicit vertical centering')
                    if pr is not None and pr.get('marT') != pr.get('marB'):
                        errors.append(f'{name}: table {tables} cell {index} has unequal vertical margins')
            if is_chart:
                for axis in root.findall('.//c:valAx', NS):
                    if axis.find('c:title', NS) is None:
                        review.append(f'{name}: value axis has no native title; verify an adjacent editable quantity/unit label')
                    fmt = axis.find('c:numFmt', NS)
                    if fmt is not None and fmt.get('sourceLinked') == '1':
                        review.append(f'{name}: axis number format links to source; inspect displayed precision')
    if not slides:
        errors.append('No slides found')
    return {'slide_count': slides, 'table_count': tables, 'chart_count': charts,
            'errors': sorted(set(errors)), 'manual_review': sorted(set(review)),
            'scope': 'Explicit formatting only. No visual, scientific, inherited-font or application-editability verification.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pptx')
    parser.add_argument('--chinese-font', default='Microsoft YaHei')
    parser.add_argument('--latin-font', default='Arial')
    args = parser.parse_args()
    report = audit(args.pptx, args.chinese_font, args.latin_font)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(1 if report['errors'] else 0)
