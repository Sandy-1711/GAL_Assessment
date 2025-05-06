# Step 1: Build the React application
FROM node:19.8.1 AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY frontend/package.json frontend/package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY frontend/ ./

# Build the React app
RUN npm run build

# Step 2: Serve the React app using a lightweight web server
FROM nginx:alpine

# Copy the Next.js build output (from the .next folder) to Nginx's serving directory
COPY --from=build /app/.next /usr/share/nginx/html/.next

# Copy static assets (optional, if you have static files)
COPY --from=build /app/public /usr/share/nginx/html/public

# Expose port 80 to access the app
EXPOSE 80

# Run Nginx server
CMD ["nginx", "-g", "daemon off;"]
