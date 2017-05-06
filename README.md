# singularity-jupyter
This example show how to run a jupyter notebook server within singularity container.

## Create and bootstrap the container

```bash
$ sudo singularity create -s 1200 jupyter.img
$ sudo singularity bootstrap jupyter.img Singularity 
```

## Use singularity-hub to pull this container


## Run the container

```bash
$ singularity run jupyter.img
```

This will start jupyter server on port 8888. The current directory will be used as the notebook direcory.
You can connect to the server and select the notebook file [python_heat2d.ipynb](python_heat2d.ipynb). 

