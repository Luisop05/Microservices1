# jenkins/Dockerfile
FROM jenkins/jenkins:lts

# Cambia al usuario root temporalmente para instalar paquetes
USER root

# Establecer un shell debug para mayor verificación
SHELL ["/bin/bash", "-o", "pipefail", "-c"]


# Regresar al usuario jenkins
USER jenkins

# Establecer JAVA_HOME (opcional)
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
