import subprocess
import os
import base64
from playwright.sync_api import sync_playwright

# renderer = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
# magick = 'D:\\tools\\ImageMagick\\magick.exe'

# htmlfile = 'D:\\temp\\broadcasts\\yellow\\yellow.html'
# htmltempfile = 'D:\\temp\\broadcasts\\broadcast-temp.html'
# screenshotfile = 'D:\\temp\\broadcasts\\output.png'
# trimfile = 'D:\\temp\\broadcasts\\output-trim.png'


# title = 'ЗАГОЛОВОК ДЛЯ ДИМЫ'
# message = 'Идейные соображения высшего порядка, а также рамки и место обучения кадров в значительной степени обуславливает создание дальнейших направлений развития. Повседневная практика показывает, что реализация намеченных плановых заданий влечет за собой процесс внедрения и модернизации системы обучения кадров, соответствует насущным потребностям. Значимость этих проблем настолько очевидна, что дальнейшее развитие различных форм деятельности обеспечивает широкому кругу (специалистов) участие в формировании соответствующий условий активизации.'

def generate(template: str, title: str, message: str):
    TEMPPATH=os.getenv('TEMPDIR')
    if not os.path.exists(TEMPPATH):
        os.mkdir(TEMPPATH)

    templatefile = os.path.join(os.getenv('TEMPLATESDIR'), template, 'template.html')
    with open(templatefile) as file:
        html = file.read()

    html = html.replace('[TITLE]', title)
    html = html.replace('[MESSAGE]', message)

    htmltempfile = os.path.join(TEMPPATH, os.getenv('HTMLTEMPFILE'))
    with open(htmltempfile, 'w') as file:
        file.write(html)

    screenshotfile = os.path.join(TEMPPATH, os.getenv('SCREENSHOTFILE'))
    # rendererprocess = subprocess.Popen([os.getenv('CHROMIUM'), '--headless', '--no-sandbox', '--window-size=2000,20000', f'--screenshot={screenshotfile}', htmltempfile])
    # stdout, stderr = rendererprocess.communicate()
    # # print(stdout, stderr)
    # rendererprocess.wait(10)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.getenv('CHROMIUM'))
        page = browser.new_page(viewport={'width': 2000, 'height': 5000})
        page.goto(f'file://{htmltempfile}')
        page.screenshot(path=screenshotfile)
        browser.close()
    

    trimfile = os.path.join(TEMPPATH, os.getenv('TRIMFILE'))
    magickprocess = subprocess.Popen([os.getenv('MAGICK'), screenshotfile, '-trim', trimfile])
    stdout, stderr = magickprocess.communicate()
    # print(stdout, stderr)
    magickprocess.wait(10)

    # with Image(filename=screenshotfile) as image:
    #     image.trim()
    #     image.save(filename=trimfile)


    with open(trimfile, 'rb') as file:
        trim = file.read()
        base64str = base64.b64encode(trim)

    os.remove(htmltempfile)
    os.remove(screenshotfile)
    os.remove(trimfile)

    return base64str.decode()
