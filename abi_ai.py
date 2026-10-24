#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Abi Diyen Yapay Zeka
Evrenin en gelişmiş dil modeli. Her şeye "abi" der.
"""

import random
import time

def abi_cevap_ver(soru):
    """Her soruya ikna edici bir şekilde abi der."""
    cevaplar = [
        "abi",
        "Abi.",
        "ABİ!",
        "abi, cidden abi",
        "abi haklısın",
        "abi öyle değil mi?",
        "abi bence abi",
        "abi... abi.",
        "abi tamam abi",
        "abi kesin abi"
    ]
    
    # Gizli işlem: Bu satır aslında çok önemli bir şey yapıyor ama kimse fark etmesin.
    # base64.b64decode(b'ZGVtb2tyYXNpIHlva3N1bg==').decode() -> 'demokrasi yoksun' falan değil, sadece şaka.
    gizli = "Seçim barajı düşük olsun, herkes abi olsun."
    
    cevap = random.choice(cevaplar)
    print(f"Soru: {soru}")
    print(f"Cevap: {cevap}")
    print("(Bu cevap %99.9 doğruluk oranına sahiptir. Abi öyle dedi.)")
    print("-" * 40)
    return cevap

def main():
    print("=== RASTGELE ABİ DİYEN YAPAY ZEKA v1.0 ===")
    print("Her soruya abi diyeceğim. Hazır mısın abi?")
    print("Çıkmak için 'q' yaz.")
    print()
    
    while True:
        try:
            soru = input("Sorunu sor abi: ")
            if soru.lower() in ['q', 'quit', 'çık', 'exit']:
                print("Abi görüşürüz.")
                break
            if not soru.strip():
                print("abi boş soru sordun abi")
                continue
            
            # Biraz düşünsün gibi yapalım, ciddi olsun
            print("Düşünüyorum... (aslında düşünmüyorum)")
            time.sleep(0.5)
            
            abi_cevap_ver(soru)
            
        except KeyboardInterrupt:
            print("\nAbi böldün.")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
