.venv/scripts/activate   
pip install -r requirements.txt
reflex init
reflex export --frontend-only
Remove-Item -Path "public" -Recurse -Force
tar -xf frontend.zip -C public
Remove-Item -Path "frontend.zip" -Recurse -Force
deactivate