$tailwind = Join-Path $PSScriptRoot '..' 'tools' 'tailwindcss.exe'
& $tailwind -i ../frontend/css/tailwind.css -o ../backend/static/style.css --watch
