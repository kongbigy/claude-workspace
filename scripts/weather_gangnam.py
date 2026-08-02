"""
서울 강남구 날씨 + 미세먼지 정보를 가져와 weather.txt에 저장.
API 키 없이 네이버 날씨 검색 페이지(공개 웹페이지)를 스크래핑하는 방식.

주의: 네이버가 페이지 구조를 바꾸면 이 스크립트가 깨질 수 있음.
      실행할 때마다 weather.txt를 덮어씀 (누적 기록 아님).
"""

import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

QUERY_URL = "https://search.naver.com/search.naver?query=강남구+날씨"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUTPUT_PATH = "weather.txt"


def fetch_weather():
    res = requests.get(QUERY_URL, headers=HEADERS, timeout=10)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    temp_el = soup.select_one(".temperature_text")
    condition_el = soup.select_one(".weather_text")
    dust_items = soup.select(".today_chart_list .item_today")

    if not temp_el or not condition_el or len(dust_items) < 2:
        raise RuntimeError("페이지 구조가 변경된 것 같습니다. 선택자 확인이 필요합니다.")

    temperature = temp_el.get_text(strip=True).replace("현재 온도", "")
    condition = condition_el.get_text(strip=True)
    fine_dust = dust_items[0].get_text(" ", strip=True)      # 예: "미세먼지 좋음"
    ultra_fine_dust = dust_items[1].get_text(" ", strip=True)  # 예: "초미세먼지 좋음"

    return {
        "temperature": temperature,
        "condition": condition,
        "fine_dust": fine_dust,
        "ultra_fine_dust": ultra_fine_dust,
    }


def main():
    try:
        data = fetch_weather()
    except Exception as e:
        print(f"[오류] 날씨 정보를 가져오지 못했습니다: {e}", file=sys.stderr)
        sys.exit(1)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        f"조회 시각: {now}",
        "지역: 서울 강남구",
        f"기온: {data['temperature']}",
        f"날씨: {data['condition']}",
        f"{data['fine_dust']}",
        f"{data['ultra_fine_dust']}",
    ]
    content = "\n".join(lines) + "\n"

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(content)
    print(f"-> {OUTPUT_PATH} 에 저장 완료")


if __name__ == "__main__":
    main()
