from typing import List
import argparse
import os
from factory.factory import Factory

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("class_name")
    args = parser.parse_args()

    class_name = args.class_name  # listfactory.listfactory.ListFactory
    factory = Factory.get_factory(class_name)
    print(factory)

    google_link = factory.create_link('Google', 'https://www.google.com/')
    jp_yahoo_link = factory.create_link('Yahoo! JAPAN', 'https://www.yahoo.co.jp/')
    us_yahoo_link = factory.create_link('Yahoo!', 'https://www.yahoo.com/')

    yahoo_tray = factory.create_tray('Yahoo!')
    yahoo_tray.add(jp_yahoo_link)
    yahoo_tray.add(us_yahoo_link)

    search_tray = factory.create_tray('サーチエンジン')
    search_tray.add(yahoo_tray)
    search_tray.add(google_link)

    page = factory.create_page('LinkPage', 'Sadistica')
    page.add(search_tray)
    page.output()
