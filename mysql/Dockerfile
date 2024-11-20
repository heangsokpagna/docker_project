# Base image
FROM mysql:5.7

# Set root password and database in environment variables
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=testdb

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s \
    CMD mysqladmin ping -h localhost || exit 1

# Expose port 5655
EXPOSE 5655