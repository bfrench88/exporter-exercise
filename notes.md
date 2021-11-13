Ran into issues configuring Docker in rootless mode on my Linux machine, which prevent me from running minikube. Tried various fix but ran out of the time I had available for this exercise.

```
➜  ~ docker context use rootless
rootless
Current context is now "rootless"
➜  ~ sudo minikube start --driver=docker --container-runtime=containerd
😄  minikube v1.24.0 on Ubuntu 20.04
✨  Using the docker driver based on user configuration
🛑  The "docker" driver should not be used with root privileges.
💡  If you are running minikube within a VM, consider using --driver=none:
📘    https://minikube.sigs.k8s.io/docs/reference/drivers/none/

❌  Exiting due to DRV_AS_ROOT: The "docker" driver should not be used with root privileges.
```
