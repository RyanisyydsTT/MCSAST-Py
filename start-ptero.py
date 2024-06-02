import subprocess
print("Starting Server")
subprocess.run([
  "java",
  f"-Xms{ram}M", f"-Xmx{ram}M",
  "--add-modules=jdk.incubator.vector",
  "-jar", "server.jar",
  "--nogui"
])
