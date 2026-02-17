from uuid import uuid4
import zipfile

from js_generator import get_js


def _generate_manifest(name, has_css=False):
    manifest = [
        '{',
        '   "manifest_version":3,',
        f'   "name": "{name}",',
        '   "version":"1.0",',
        '   "description": "Get pranked frfr",',
        '   "content_scripts": [',
        '       {',
        '           "matches": ["<all_urls>"],',
        '           "js": ["main.js"]'
    ]

    if has_css:
        manifest[-1] = manifest[-1] + ','
        manifest.append('           "css": ["main.css"]')

    manifest += [
        '       }',
        '   ]',
        '}'
    ]

    return '\n'.join(manifest)


def generate_extension():
    name = str(uuid4())

    with zipfile.ZipFile('extensions/' + name + '.zip', 'w') as z:
        z.writestr('manifest.json', _generate_manifest(name))
        z.writestr('main.js', get_js())

    return name



if __name__ == '__main__':
    print(generate_extension())