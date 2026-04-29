#!/data/data/com.termux/files/usr/bin/bash
cd ~/TitaniumOne
mkdir -p backups
name="backup_$(date +%Y%m%d_%H%M%S).tar.gz"
tar --exclude=backups -czf backups/$name .
echo "✅ SAVED backups/$name"
