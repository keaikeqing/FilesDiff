import hashlib


def hash_file(filepath, algorithm):
    hash_alg = hashlib.new(algorithm)
    with open(filepath, 'rb') as file:
        # 分块读取文件内容进行哈希，以避免大文件的内存问题
        for chunk in iter(lambda: file.read(4096), b""):
            hash_alg.update(chunk)
    return hash_alg.hexdigest()


def compare_files(file1_path, file2_path):
    algorithms = ['md5', 'sha1', 'sha256', 'sha512', 'sha3_256', 'sha3_512']
    hashes_file1 = {alg: hash_file(file1_path, alg) for alg in algorithms}
    hashes_file2 = {alg: hash_file(file2_path, alg) for alg in algorithms}

    # 比较两个文件在所有算法下的哈希值
    for alg in algorithms:
        if hashes_file1[alg] != hashes_file2[alg]:
            print(f"Files differ in {alg.upper()} hash.")
            return False

    print("Files are identical in all hash algorithms.")
    return True


if "__name__" == "__main__":
    # 使用示例（你需要替换这些路径为实际的文件路径）:
    path1 = '/path/to/file1'
    path2 = '/path/to/file2'
    compare_files(path1, path2)
