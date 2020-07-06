import os
from pagemaker.pagemaker import PageMaker

if __name__ == '__main__':

    base_dir = os.path.dirname(__file__)
    file_name = 'sample.html'
    
    # シンプルな窓口だけをAPIとして公開し複雑な処理は秘匿する
    # -> 少ないインターフェース
    PageMaker.make_welcome_page('sadistica@ut.ac.jp', base_dir + '/' + file_name)