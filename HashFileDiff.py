import hashlib


def hash_file(filepath, algorithm):
    hash_alg = hashlib.new(algorithm)
    try:
        with open(filepath, 'rb') as file:
            # 分块读取文件内容进行哈希，以避免大文件的内存问题
            for chunk in iter(lambda: file.read(4096), b""):
                hash_alg.update(chunk)
        return hash_alg.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        raise


def compare_files(alg, hash_value, file_path):
    try:
        hashes_file = hash_file(file_path, alg)

        # 比较文件哈希值和给定的哈希值
        if hashes_file != hash_value:
            print(f"Files differ in {alg.upper()} hash.")
            return False

        print("Files are identical in all hash algorithms.")
        return True
    except FileNotFoundError:
        # 处理文件未找到异常
        print("An error occurred due to a missing file.")
        return False



if __name__ == "__main__":
    # 替换这些路径为实际的文件路径
    path = 'C:\\Users\mzq\Desktop\Clash.for.Windows-0.20.39-x64-linux.tar.gz'
    # 使用哈希算法如 'md5', 'sha1', 'sha256', 'sha512', 'sha3_256', 'sha3_512'
    # 可添加多个算法对比
    algorithms = ['sha256']
    # 需要对比的哈希值
    HashValue = ['e07c5e358bce99511c103262ba0d6d0167c70242f2e68827b09f7a2918d43dc0']
    for alg_id in range(len(algorithms)):
        compare_files(algorithms[alg_id], HashValue[alg_id], path)
