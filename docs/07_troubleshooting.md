Troubleshooting:

27 Sep 2024
1. **Challenge**: Error with `aries-cloudagent` startup due to missing required arguments (`--inbound-transport`).
   - **Solution**: Updated command to include `--inbound-transport` and `--outbound-transport` options. The agent started but encountered a new error regarding the genesis URL.

2. **Challenge**: Issue with `openssl-sys` during `libindy` compilation. Error message indicated missing OpenSSL headers.
   - **Solution**: Installed `libssl-dev` on Ubuntu, set `OPENSSL_DIR`, and ensured the correct version of `libindy` dependencies were installed.

3. **Challenge**: Conflicting values for `Trusted` option in `apt` while adding the Sovrin repository.
   - **Solution**: Removed conflicting sources and re-added the Sovrin repository with correct configuration.

4. **Challenge**: Docker container for `von-network` kept exiting immediately upon startup.
   - **Solution**: Checked logs and removed unused images/containers. Also ran containers in interactive mode to debug issues.

5. **Challenge**: `libindy` dependency issue with `libssl1.1` not being installable on newer Ubuntu versions.
   - **Solution**: Downgraded dependencies or manually installed compatible OpenSSL versions.

6. **Challenge**: Docker Compose installation issue. `docker-compose` was missing or not executable.
   - **Solution**: Re-downloaded Docker Compose, ensured it was installed in `/usr/local/bin`, made it executable, and added the correct path to `PATH`.

7. **Challenge**: Connection refused to `localhost:9000` when trying to access genesis transactions.
   - **Solution**: Verified that the `von-network` container was running, checked container logs, and ensured that no other services were using port `9000`.

8. **Challenge**: `aries-cloudagent` failed to retrieve genesis transactions due to a temporary failure in name resolution (`von-network`).
   - **Solution**: Added `depends_on` in Docker Compose to ensure `von-network` starts before `aries-cloudagent`, checked network setup, and rebuilt Docker environment.

9. **Challenge**: Docker Compose encountered errors pulling the `von-network-base` image, resulting in a "pull access denied" error.
   - **Solution**: Verified the image name, changed it to the correct `bcgovimages/von-network` image, and logged in to Docker Hub for access.

10. **Challenge**: Port `9000` was inaccessible, causing `curl` commands and `aries-cloudagent` to fail to connect to the Indy ledger.
    - **Solution**: Checked for port conflicts using `lsof`, changed the port in `docker-compose.yml`, and verified the binding of ports in Docker.

26 Sep 2024

### Challenges Faced & Solutions Tried in Mapping Ports from UTM Ubuntu Server Inside Mac

1. **Challenge:** Mapping external ports to the UTM VM running Ubuntu Server.
   - **Solution:** Use UTM’s built-in port forwarding feature to redirect specific ports from the host (Mac) to the guest (Ubuntu) by configuring port forwarding rules in UTM's network settings.

2. **Challenge:** Finding the correct IP address and port within the Ubuntu server for forwarding.
   - **Solution:** Ensure the service inside Ubuntu is bound to the correct internal IP (e.g., `10.0.2.15`) or `0.0.0.0` to listen on all interfaces, and identify the port used by the service (e.g., port 80 for a web server).

3. **Challenge:** Understanding the difference between host and guest port mappings.
   - **Solution:** Clearly specify the host-side port (e.g., `127.0.0.1:8080`) for local Mac access and the guest-side port (e.g., `10.0.2.15:80`) for the service running in Ubuntu.

4. **Challenge:** Making sure traffic on the Mac is correctly forwarded to the service in the VM.
   - **Solution:** Double-check UTM settings for correct port forwarding rules and ensure that no local firewall (on either the Mac or Ubuntu server) is blocking the traffic.

5. **Challenge:** Accessing services running on Ubuntu VM from macOS after forwarding ports.
   - **Solution:** Access services using `localhost:host_port` (e.g., `localhost:8080` for web services) on macOS once port forwarding is set up, verifying that services are available from the specified port.

6. **Challenge:** Firewall blocking ports in Ubuntu or macOS.
   - **Solution:** Ensure that the firewall on both Ubuntu and macOS allows traffic on the required ports, or disable the firewall for testing.

7. **Challenge:** Service not accessible on the forwarded port due to binding issues.
   - **Solution:** Bind services in Ubuntu to `0.0.0.0` or the correct internal IP address (`10.0.2.15`), allowing traffic from any network interface.

25 Sep 2024

### Challenges Faced:
1. **Failed OpenSSL Build**: The custom build command for `openssl-sys v0.9.59` failed with exit status 101.
2. **Unset Environment Variables**: Key environment variables like `OPENSSL_LIB_DIR` and `OPENSSL_INCLUDE_DIR` were unset, causing the build to fail.
3. **Missing OpenSSL Library Path**: The build script expected OpenSSL in `/usr/local/opt/lib`, but the directory did not exist.
4. **AARCH64 Apple Darwin Environment**: OpenSSL paths needed to be configured specifically for Apple Silicon (AARCH64).

### Solutions Tried/To Try:
1. **Install OpenSSL**: Use Homebrew to install OpenSSL:
   ```bash
   brew install openssl
   ```
2. **Set Environment Variables**: Export the necessary OpenSSL paths based on the Homebrew installation location:
   ```bash
   export OPENSSL_DIR=$(brew --prefix openssl)
   export OPENSSL_LIB_DIR=$(brew --prefix openssl)/lib
   export OPENSSL_INCLUDE_DIR=$(brew --prefix openssl)/include
   ```
3. **Retry Build**: Attempt to rebuild the project after setting the environment variables:
   ```bash
   cargo build
   ```
4. **Verify OpenSSL Installation**: Confirm the OpenSSL installation by checking its version:
   ```bash
   openssl version
   ```
5. **Modify Cargo Configuration** (optional): If the issue persists, add the correct OpenSSL paths to the `.cargo/config` file:
   ```toml
   [target.aarch64-apple-darwin]
   rustflags = ["-L", "/opt/homebrew/opt/openssl/lib", "-I", "/opt/homebrew/opt/openssl/include"]
   ``` 

24 Sep 2024

### **Challenges Faced**:
1. **Obsolete `version` field in Docker Compose file**:
   - The attribute `version` in your `docker-compose.yml` is marked as obsolete, potentially causing confusion.
   
2. **Docker daemon not running**:
   - Error: "Cannot connect to the Docker daemon at unix:///Users/gvsh/.docker/run/docker.sock."
   
3. **Issues running Indy on macOS**:
   - Compatibility issues when trying to run Indy on macOS, especially related to Linux dependencies or services like Indy SDK.

### **Solutions Tried**:

1. **Obsolete Docker Compose `version` field**:
   - **Solution**: Remove the `version` field from the `docker-compose.yml` file, as it is no longer required in newer versions of Docker Compose.

2. **Docker daemon not running**:
   - **Solution 1**: Start **Docker Desktop** on macOS to ensure the Docker daemon is running. The whale icon in the menu bar should stop animating once Docker is ready.
   - **Solution 2**: Verify Docker is running by running `docker info` in the terminal. If the daemon is running, it should return information about the Docker environment.
   - **Solution 3**: Fix Docker socket permissions if the error persists by running `sudo chown $USER /var/run/docker.sock`.
   - **Solution 4**: Restart Docker Desktop or enable Docker to start automatically upon login from **Docker Desktop Preferences**.

3. **Running Indy on macOS**:
   - **Solution 1: Use a Linux Virtual Machine (VM)**:
     - Install and use **UTM** or **VirtualBox** to run a full Linux environment inside macOS.
     - Create a VM with Ubuntu or another Linux distribution and install the necessary Indy SDK dependencies.
   - **Solution 2: Use Docker**:
     - Run Linux containers via Docker to simulate a Linux environment for services like Indy. For example, run `docker run -it ubuntu bash` to interact with an Ubuntu container.
   - **Solution 3: Use Multipass for Ubuntu**:
     - Install **Multipass** for a lightweight, fast Ubuntu VM. This allows easy access to a Linux environment for development tasks related to Indy.