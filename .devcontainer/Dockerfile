FROM quay.io/jupyter/minimal-notebook:python-3.11

USER root

# Generally, Dev Container Features assume that the non-root user (in this case jovyan)
# is in a group with the same name (in this case jovyan). So we must first make that so.
RUN groupadd jovyan \
    && usermod -g jovyan -a -G users jovyan

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

RUN apt-get update && apt-get -y install --no-install-recommends libgl1-mesa-glx

USER jovyan

RUN mamba install --yes \
    'cadquery=2.4.0' \
    'ocp=7.7.2.1' && \
    mamba clean --all -f -y

RUN pip install --no-cache-dir cqkit==0.5.6
