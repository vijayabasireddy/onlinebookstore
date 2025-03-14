# Use Tomcat as the base image
FROM tomcat:9.0-jdk17

# Copy the pre-built WAR file into the Tomcat webapps directory
COPY target/onlinebookstore.war /usr/local/tomcat/webapps/onlinebookstore.war

# Start Tomcat
CMD ["catalina.sh", "run"]

