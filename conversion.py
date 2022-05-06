from PIL import Image
import glob
import os

# 変換前の画像を格納したフォルダ名
original_folder = 'original/'
# 変換後の画像を格納したフォルダ名
conv_folder = 'convert/'

# 画像サイズ（幅）を指定
desktop_size = [218, 284, 349, 415, 480, 546, 611, 677, 742, 808, 873]
tablet_size = [150, 195, 240, 285, 330, 375, 420, 465, 510, 555, 600]
smartphone_size = [92, 120, 148, 175, 203, 231, 258, 286, 314, 341, 369]
modal_size = [1200, 2400]
loading_size = [50]

# 画像サイズ（高さ）を指定
height = 10000

# 出力する画像タイプを指定
output_x1 = True
output_x2 = True
output_x3 = False
modal = False

# フォーマット変換の画質を指定
jpg_quality = 75    # 1〜95を設定（デフォルトは75）
webp_quality = 80   # 1〜100を設定（デフォルトは80）

# 画像パスを取得
files = glob.glob(original_folder + "*")

print('======== 開始 ========')

# 画像をリサイズ
for file in files:
    # 前処理
    file_name = os.path.splitext(os.path.basename(file))[0]
    img = Image.open(file).convert('RGB')

    print(file_name)

    # ファイル名を設定
    target = '('
    index = file_name.find(target)
    if file_name[index-1] == '_':
        new_file_name = file_name[:index-1]
    else:
        new_file_name = file_name[:index]

    # デスクトップ
    if 'Desktop' in file_name:

        # 各サイズで処理
        for size in desktop_size:
            # 各解像度で処理
            if output_x1:

                width = size
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-pc-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-pc-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

            if output_x2:

                width = size*2
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-pc-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-pc-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

            if output_x3:

                width = size*3
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-pc-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-pc-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

        if modal:

            # モーダル用
            for size in modal_size:

                width = size
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-pc-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-pc-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

        # ローディング用
        for size in loading_size:

            width = size
            # リサイズ
            new_img = img.copy()
            new_img.thumbnail((width, height))

            # フォーマット変換（JPEG）
            new_img.save(conv_folder + new_file_name + '-pc-' +
                         str(width) + '.jpg', quality=jpg_quality, optimize=True)

    # タブレット
    elif 'iPad' in file_name:
        # 各サイズで処理
        for size in tablet_size:
            # 各解像度で処理
            if output_x1:

                width = size
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-tb-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-tb-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

            if output_x2:

                width = size*2
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-tb-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-tb-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

            if output_x3:

                width = size*3
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-tb-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-tb-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

            # ローディング用
        for size in loading_size:

            width = size
            # リサイズ
            new_img = img.copy()
            new_img.thumbnail((width, height))

            # フォーマット変換（JPEG）
            new_img.save(conv_folder + new_file_name + '-tb-' +
                         str(width) + '.jpg', quality=jpg_quality, optimize=True)

    # スマートフォン
    elif 'iPhone' in file_name:
        # 各サイズで処理
        for size in smartphone_size:
            # 各解像度で処理
            if output_x1:

                width = size
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-sp-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-sp-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

            if output_x2:

                width = size*2
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-sp-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-sp-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

            if output_x3:

                width = size*3
                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（JPEG）
                new_img.save(conv_folder + new_file_name + '-sp-' +
                             str(width) + '.jpg', quality=jpg_quality, optimize=True)

                # リサイズ
                new_img = img.copy()
                new_img.thumbnail((width, height))

                # フォーマット変換（WebP）
                new_img.save(conv_folder + new_file_name + '-sp-' +
                             str(width) + '.webp', quality=webp_quality, optimize=True)

        # ローディング用
        for size in loading_size:

            width = size
            # リサイズ
            new_img = img.copy()
            new_img.thumbnail((width, height))

            # フォーマット変換（JPEG）
            new_img.save(conv_folder + new_file_name + '-sp-' +
                         str(width) + '.jpg', quality=jpg_quality, optimize=True)

print('======== 終了 ========')
