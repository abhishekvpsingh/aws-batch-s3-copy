import os
import sys
import boto3

def must(name: str) -> str:
    v = os.getenv(name)
    if not v:
        print(f"Missing required env var: {name}", file=sys.stderr)
        sys.exit(2)
    return v

def main():
    src_bucket = must("SRC_BUCKET")
    src_key    = must("SRC_KEY")
    dst_bucket = must("DST_BUCKET")
    dst_key    = os.getenv("DST_KEY") or src_key.split("/")[-1]  # default: keep filename

    s3 = boto3.client("s3")
    print(f"Copying s3://{src_bucket}/{src_key} -> s3://{dst_bucket}/{dst_key}")

    copy_source = {"Bucket": src_bucket, "Key": src_key}
    s3.copy_object(Bucket=dst_bucket, Key=dst_key, CopySource=copy_source)

    print("Done ✅")

if __name__ == "__main__":
    main()
