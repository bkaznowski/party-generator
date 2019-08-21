FROM python:3.6
RUN pip install Pillow
RUN pip install numpy
RUN pip install blend_modes
WORKDIR /party_generator
COPY party_generator.py .
CMD ["python", "party_generator.py"]
