# singularity-jupyter
This example show how to run a jupyter notebook server within singularity container.

## Create and bootstrap the container

```bash
$ sudo singularity create -s 1200 jupyter.img
$ sudo singularity bootstrap jupyter.img Singularity 
```
