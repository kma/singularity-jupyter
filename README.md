# singularity-jupyter
This example show how to run a jupyter notebook server within singularity container.

## Create and bootstrap the container

```bash
$ sudo singularity create -s 1200 jupyter.img
$ sudo singularity bootstrap jupyter.img Singularity 
```

## Run the container

```bash
$ singularity run jupyter.img
```

This will start jupyter server on port 8888. The current directory will be used as the notebook direcory.

## Use singularity-hub to pull this container

```bash

```

