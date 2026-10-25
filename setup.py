from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    author='Tu Nombre',
    description='Una aplicación de detección de emociones utilizando Watson NLP',
)