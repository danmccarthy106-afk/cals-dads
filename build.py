# Builds index.html from the master page source (SRC) by wrapping it in a full HTML document
# and injecting the Firebase config. Run: python3 build.py [path-to-source.html]
import sys
SRC = sys.argv[1] if len(sys.argv) > 1 else 'src.html'
src = open(SRC, encoding='utf-8').read().replace('<meta charset="utf-8">\n', '', 1)
head_end = src.index('</style>') + len('</style>')
head, body = src[:head_end], src[head_end:]
cfg = '{"projectId":"essence-trip-planner-2026","appId":"1:394125240589:web:ec8cd7feef54a8e29a6844","apiKey":"AIzaSyB8zfz1iBpKsY2JDwChUUkZM90bPckNy1Y","authDomain":"essence-trip-planner-2026.firebaseapp.com"}'
assert '/*FIREBASE_CONFIG*/null' in body
body = body.replace('/*FIREBASE_CONFIG*/null', cfg, 1)
fb = ('<script src="https://www.gstatic.com/firebasejs/10.14.1/firebase-app-compat.js"></script>\n'
      '<script src="https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore-compat.js"></script>\n')
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏰</text></svg>">\n'
       + head + '\n</head>\n<body>\n' + fb + body + '\n</body>\n</html>\n')
open('index.html', 'w', encoding='utf-8').write(out)
print(len(out), 'bytes')
