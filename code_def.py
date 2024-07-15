import subprocess
import platform
import os
import re
import sys




system = platform.system()

def error(message):
    print(f'Error: {message}')
    os._exit(1)




def check_java_version():
    supported_ver = [17, 18, 19, 20, 21, 22]
    
    try:
        if system == 'Windows':
            java_version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT, text=True)
        elif system == 'Linux':
            java_version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT, shell=True, text=True)
        else:
            error("Unsupported operating system.")
    except subprocess.CalledProcessError:
        print("Java is not installed or not found in the system PATH, proceeding anyways")
    java_version_match = re.search(r'\"(\d+)\.(\d+)\.(\d+)_\d+\"', java_version)
    if java_version_match:
        java_version_num = int(java_version_match.group(1))
        if java_version_num in supported_ver:
            return True
    return False

def download_file(url, filename):
    subprocess.run(['curl', '-O', url], check=True)

def setup_paper_server(ver, build_num):
    url = f'https://api.papermc.io/v2/projects/paper/versions/{ver}/builds/{build_num}/downloads/paper-{ver}-{build_num}.jar'
    filename = f'paper-{ver}-{build_num}.jar'
    download_file(url, filename)
    os.rename(os.path.join(filename), os.path.join('server.jar'))
    print("Download Done!")
    print("Installing!")
    print("Aikar’s flag? Recommended and high performance server script")
    Aikar = input("Type Y/N: ")
    if (Aikar == "y" or Aikar == "Y") and system == "Windows":
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()    
    if (Aikar == "y" or Aikar == "Y") and system == "Linux":
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()    
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()   
    print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

def setup_purpur_server(ver, build_num):
    url = f'https://api.purpurmc.org/v2/purpur/{ver}/{build_num}/download'
    filename = 'download'
    download_file(url, filename)
    os.rename(os.path.join(filename), os.path.join('server.jar'))
    print("Download Done!")
    print("Installing!")
    print("Aikar’s flag? Recommended and high performance server script")
    Aikar = input("Type Y/N: ")
    if (Aikar == "y" or Aikar == "Y") and system == "Windows":
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()    
    if (Aikar == "y" or Aikar == "Y") and system == "Linux":
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()    
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()   
    print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

def setup_pufferfish_server(ver, build_num):
    if "1.20" in ver:
        url = f'https://ci.pufferfish.host/job/Pufferfish-1.20/{build_num}/artifact/build/libs/pufferfish-paperclip-{ver}-R0.1-SNAPSHOT-reobf.jar'
    elif "1.19" in ver:
        url = f'https://ci.pufferfish.host/job/Pufferfish-1.19/{build_num}/artifact/build/libs/pufferfish-paperclip-{ver}-R0.1-SNAPSHOT-reobf.jar'
    elif "1.18" in ver:
        url = f'https://ci.pufferfish.host/job/Pufferfish-1.18/{build_num}/artifact/build/libs/pufferfish-paperclip-{ver}-R0.1-SNAPSHOT-reobf.jar'
    elif "1.17" in ver:
        url = f'https://ci.pufferfish.host/job/Pufferfish-1.17/{build_num}/artifact/build/libs/pufferfish-paperclip-{ver}-R0.1-SNAPSHOT-reobf.jar'
    filename = f'pufferfish-paperclip-{ver}-R0.1-SNAPSHOT-reobf.jar'
    download_file(url, filename)
    os.rename(os.path.join(filename), os.path.join('server.jar'))
    print("Download Done!")
    print("Installing!")
    print("Aikar’s flag? Recommended and high performance server script")
    Aikar = input("Type Y/N: ")
    if (Aikar == "y" or Aikar == "Y") and system == "Windows":
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()    
    if (Aikar == "y" or Aikar == "Y") and system == "Linux":
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()    
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()   
    print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

def setup_velocity_server(ver, build_num):
    url = f'https://api.papermc.io/v2/projects/velocity/versions/{ver}/builds/{build_num}/downloads/velocity-{ver}-{build_num}.jar'
    filename = f'velocity-{ver}-{build_num}.jar'
    download_file(url, filename)
    os.rename(os.path.join(filename), os.path.join('server.jar'))
    print("Download Done!")
    print("Installing!")
    print("Custom flag? Recommended and high performance server script")
    flag = input("Type Y/N: ")
    if (flag == "y" or flag == "Y") and system == "Windows":
        runscript = "java -Xms4096M -Xmx4096M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()    
    if (flag == "y" or flag == "Y") and system == "Linux":
        runscript = "java -Xms4096M -Xmx4096M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()    
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()   
    print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

def setup_bungee_server():
    url = 'https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/'
    filename = 'BungeeCord.jar'
    download_file(url, filename)
    os.rename(os.path.join(filename), os.path.join('server.jar'))
    print("Download Done!")
    print("Installing!")
    print("Custom flag? Recommended and high performance server script")
    flag = input("Type Y/N: ")
    if (flag == "y" or flag == "Y") and system == "Windows":
        runscript = "java -Xms4096M -Xmx4096M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()    
    if (flag == "y" or flag == "Y") and system == "Linux":
        runscript = "java -Xms4096M -Xmx4096M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()    
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()   
    print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

def setup_waterfall_server(ver, build_num):
    url = f'https://api.papermc.io/v2/projects/waterfall/versions/{ver}/builds/{build_num}/downloads/waterfall-{ver}-{build_num}.jar'
    filename = f'waterfall-{ver}-{build_num}.jar'
    download_file(url, filename)
    os.rename(os.path.join(filename), os.path.join('server.jar'))
    print("Download Done!")
    print("Installing!")
    print("Custom flag? Recommended and high performance server script")
    flag = input("Type Y/N: ")
    if (flag == "y" or flag == "Y") and system == "Windows":
        runscript = "java -Xms4096M -Xmx4096M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()    
    if (flag == "y" or flag == "Y") and system == "Linux":
        runscript = "java -Xms4096M -Xmx4096M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()    
    else:
        runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()   
    print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

def setup_fabric_server(ver, fabric_loader_ver, fabric_installer_ver):
    url = f'https://meta.fabricmc.net/v2/versions/loader/{ver}/{fabric_loader_ver}/{fabric_installer_ver}/server/jar'
    filename = 'jar'
    download_file(url, filename)
    os.rename(os.path.join(filename), os.path.join('server.jar'))
    print("Download Done!")
    print("Installing!")
    if system == 'Windows':
        runscript = "java -Xms4096M -Xmx4096M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui"
        file = open('runserver.bat', 'a')
        file.write(runscript)
        file.close()
        print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")
    else:
        runscript = "java -Xms4096M -Xmx4096M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui"
        file = open('runserver.sh', 'a')
        file.write(runscript)
        file.close()
        print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

def setup_forge_server(ver, forge_ver):
    url = f'https://maven.minecraftforge.net/net/minecraftforge/forge/{ver}-{forge_ver}/forge-{ver}-{forge_ver}-installer.jar'
    filename = f'forge-{ver}-{forge_ver}-installer.jar'
    download_file(url, filename)
    os.rename(os.path.join(filename), os.path.join('installer.jar'))
    print("Download Done!")
    print("Installing!")
    subprocess.run(['java', '-jar', 'installer.jar', '--installServer'], check=True)
    os.rename(os.path.join(run.bat), os.path.join('runserver.bat'))
    print("Installed Successfully! Run your server by clicking the runserver.bat It might be stored in the directory that you have cd-ed")

def setup_custom_server():
    print("Please put your server.jar(rename!) into the folder you have cd-ed!")
    confirm = input("Type “OK” to proceed")
    if confirm == 'OK' or confirm == 'ok':
        print("Installing!")
        print("Aikar’s flag? Recommended and high performance server script")
        Aikar = input("Type Y/N: ")
        if (Aikar == "y" or Aikar == "Y") and system == "Windows":
            runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
            file = open('runserver.bat', 'a')
            file.write(runscript)
            file.close()
        else:
            runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
            file = open('runserver.bat', 'a')
            file.write(runscript)
            file.close()    
        if (Aikar == "y" or Aikar == "Y") and system == "Linux":
            runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
            file = open('runserver.sh', 'a')
            file.write(runscript)
            file.close()    
        else:
            runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
            file = open('runserver.sh', 'a')
            file.write(runscript)
            file.close()   
        print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

    else:
        setup_custom_server()
def setup_van_server():
    print("Downlod the version from https://mcversions.net/")
    print("Please put your server.jar(rename!) into the folder you have cd-ed!")
    confirm = input("Type “OK” to proceed")
    if confirm == 'OK' or confirm == 'ok':
        print("Installing!")
        print("Aikar’s flag? Recommended and high performance server script")
        Aikar = input("Type Y/N: ")
        if (Aikar == "y" or Aikar == "Y") and system == "Windows":
            if Aikar == "y" or "Y" and system == "Windows":
                runscipt = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
                file = open('runserver.bat', 'a')
                file.write(runscipt)
                file.close()
            elif Aikar == "n" or "N" and system == "Windows":
                runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
                file = open('runserver.bat', 'a')
                file.write(runscipt)
                file.close()    
        if Aikar == "y" or "Y" and system == "Linux" or "OSX":
            # 
            runscipt = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -jar server.jar --nogui"
            file = open('runserver.sh', 'a')
            file.write(runscipt)
            file.close()    
        elif Aikar == "n" or "N" and system == "Linux" or "OSX":
            runscript = "java -Xms4096M -Xmx4096M --add-modules=jdk.incubator.vector -jar server.jar --nogui"
            file = open('runserver.sh', 'a')
            file.write(runscipt)
            file.close()   
        print("Installed Successfully! Run your server by clicking the runserver.bat/sh It might be stored in the directory that you have cd-ed")

    else:
        setup_van_server()

def run():

    if not check_java_version():
        print("Java Installed Incorrectly, or you haven't installed it, proceeding anyway...")

    print("Java Installed! Choose a version you want to install!")
    print("""
          """)
    print("Choose the version you want to install!")
    print("""
Plugin Server:
    1. Paper
    2. Purpur
    3. PufferFish
Proxy Server:
    4. Velocity
    5. Bungeecord
    6. Waterfall
Mod Server:
    7. Fabric
    8. Forge
Other Server:
    9. Vanilla (Original)
    10. Custom
        """)
    
    ver_choice = input("Select: ")

    if ver_choice == '1':
        ver = input("Input the Paper version you want to install: ")
        build_num = input("Input the version's build number (You can find it in build explorer): ")
        setup_paper_server(ver, build_num)
    elif ver_choice == '2':
        ver = input("Input the Purpur version you want to install: ")
        build_num = input("Input the version's build number (You can find it in build explorer): ")
        setup_purpur_server(ver, build_num)
    elif ver_choice == '3':
        ver = input("Input the Pufferfish version you want to install: ")
        build_num = input("Input the version's build number (You can find it in build explorer): ")
        setup_pufferfish_server(ver, build_num)
    elif ver_choice == '4':
        ver = input("Input the Velocity version you want to install(If it’s a snapshot version, add a “-SNAPSHOT“ at the end): ")
        build_num = input("Input the version's build number (You can find it in build explorer): ")        
        setup_velocity_server(ver, build_num)
    elif ver_choice == '5':
        setup_bungee_server()
    elif ver_choice == '6':
        ver = input("Input the Minecraft version you want to install: ")
        build_num = input("Input the version's build number (You can find it in build explorer): ")
        setup_waterfall_server(ver, build_num)
    elif ver_choice == '7':
        ver = input("Input the Minecraft version you want to install: ")
        fabric_loader_ver = input("Input the version of loader: ")
        fabric_installer_ver = input("Input the version of installer: ")
        setup_fabric_server(ver, fabric_loader_ver, fabric_installer_ver)
    elif ver_choice == '8':
        print("Forge now only support Windows, check github latest update!")
        ver = input("Input the Minecraft version you want to install: ")
        forge_ver = input("Input the Forge version you want to install: ")
        setup_forge_server(ver, forge_ver)
    elif ver_choice == '9':
        setup_van_server()
    elif ver_choice == '10':
        setup_custom_server()


