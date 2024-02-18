def build_url(bucket_path):
    return f'https://lcchallenge.blob.core.windows.net/lc-challenge/{bucket_path}'

def sign_url(url, token):
    return f'{url}?{token}'