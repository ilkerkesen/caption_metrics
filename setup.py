from setuptools import setup


with open('README.md', 'r') as fh:
    readme = fh.read()


setup(
    name='caption_metrics',
    version='0.9',
    maintainer='ilkerkesen',
    description='Package for Image Captioning Evaluation Metrics',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ilkerkesen/caption_metrics',
    license='MIT',
    packages=['caption_metrics'],
    package_data={'': ['*.jar', '*.gz']},
    install_requires=['pycocotools>=2.0.2', 'numpy'],
    zip_safe=False,
    include_package_data=True,
)