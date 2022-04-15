import os

def count_all_files(path):
    cnt = {'size': 0, 'dirs': 0, 'files': 0}

    for elm in os.listdir(path):
        if elm in ['.git', '.idea']:
            continue

        abspath = path + '/' + elm
        if os.path.isdir(abspath):
            cnt['dirs'] += 1
            temp_cnt = count_all_files(abspath)
            cnt['size'] += temp_cnt['size']
            cnt['dirs'] += temp_cnt['dirs']
            cnt['files'] += temp_cnt['files']
        else:
            cnt['files'] += 1
            cnt['size'] += os.path.getsize(abspath)

    return cnt

print(count_all_files(os.path.abspath('../..')))
