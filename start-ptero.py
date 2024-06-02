import subprocess
import code_def
print("Starting Server")
subprocess.run([
  "java",
  f"-Xms{code_def.ram}M", f"-Xmx{code_def.ram}M",
  "--add-modules=jdk.incubator.vector",
  "-jar", "server.jar",
  "--nogui"
])
