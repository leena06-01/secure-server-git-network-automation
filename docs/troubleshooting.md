## DNS Resolution Failure

### Symptom
A hostname cannot be resolved to an IP address.

### Test
Use Python socket.gethostbyname() with a hostname.

### Expected Failure
An invalid hostname returns a DNS resolution error.

### Troubleshooting
1. Check the hostname for typing errors.
2. Test a known hostname.
3. Check DNS configuration and resolver availability.
4. Check network connectivity.

### Lesson
DNS resolution, network connectivity, and service availability are separate checks.
