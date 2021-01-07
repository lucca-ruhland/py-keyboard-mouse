import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keyboard-mouse",
    version="0.0.1",
    author="Lucca Ruhland",
    author_email="lucca.ruhland@gmx.net",
    description="mouse emulation via keyboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages('src', exclude=["*tests"]),
    package_dir={"": "src"},
    install_requires=[
        "keyboard",
        "pyautogui",
    ],
    entry_points={
        "console_scripts": [
            "keyboard-mouse = keyboard_mouse.main:main"
        ]
    }
)
