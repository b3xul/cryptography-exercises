from base64 import b64decode
import numpy
from string import *



# from CryptoPals S3C19/S3C20
# same key and same nonce: mount a keystream reuse attack
# encoded_ciphertexts = [b"SSBoYXZlIG1ldCB0aGVtIGF0IGNsb3NlIG9mIGRheQ==", b"Q29taW5nIHdpdGggdml2aWQgZmFjZXM=", b"RnJvbSBjb3VudGVyIG9yIGRlc2sgYW1vbmcgZ3JleQ==", b"RWlnaHRlZW50aC1jZW50dXJ5IGhvdXNlcy4=", b"SSBoYXZlIHBhc3NlZCB3aXRoIGEgbm9kIG9mIHRoZSBoZWFk", b"T3IgcG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==", b"T3IgaGF2ZSBsaW5nZXJlZCBhd2hpbGUgYW5kIHNhaWQ=", b"UG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==", b"QW5kIHRob3VnaHQgYmVmb3JlIEkgaGFkIGRvbmU=", b"T2YgYSBtb2NraW5nIHRhbGUgb3IgYSBnaWJl", b"VG8gcGxlYXNlIGEgY29tcGFuaW9u", b"QXJvdW5kIHRoZSBmaXJlIGF0IHRoZSBjbHViLA==", b"QmVpbmcgY2VydGFpbiB0aGF0IHRoZXkgYW5kIEk=", b"QnV0IGxpdmVkIHdoZXJlIG1vdGxleSBpcyB3b3JuOg==", b"QWxsIGNoYW5nZWQsIGNoYW5nZWQgdXR0ZXJseTo=", b"QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=", b"VGhhdCB3b21hbidzIGRheXMgd2VyZSBzcGVudA==", b"SW4gaWdub3JhbnQgZ29vZCB3aWxsLA==", b"SGVyIG5pZ2h0cyBpbiBhcmd1bWVudA==", b"VW50aWwgaGVyIHZvaWNlIGdyZXcgc2hyaWxsLg==", b"V2hhdCB2b2ljZSBtb3JlIHN3ZWV0IHRoYW4gaGVycw==", b"V2hlbiB5b3VuZyBhbmQgYmVhdXRpZnVsLA==", b"U2hlIHJvZGUgdG8gaGFycmllcnM/", b"VGhpcyBtYW4gaGFkIGtlcHQgYSBzY2hvb2w=", b"QW5kIHJvZGUgb3VyIHdpbmdlZCBob3JzZS4=", b"VGhpcyBvdGhlciBoaXMgaGVscGVyIGFuZCBmcmllbmQ=", b"V2FzIGNvbWluZyBpbnRvIGhpcyBmb3JjZTs=", b"SGUgbWlnaHQgaGF2ZSB3b24gZmFtZSBpbiB0aGUgZW5kLA==", b"U28gc2Vuc2l0aXZlIGhpcyBuYXR1cmUgc2VlbWVkLA==", b"U28gZGFyaW5nIGFuZCBzd2VldCBoaXMgdGhvdWdodC4=", b"VGhpcyBvdGhlciBtYW4gSSBoYWQgZHJlYW1lZA==", b"QSBkcnVua2VuLCB2YWluLWdsb3Jpb3VzIGxvdXQu", b"SGUgaGFkIGRvbmUgbW9zdCBiaXR0ZXIgd3Jvbmc=", b"VG8gc29tZSB3aG8gYXJlIG5lYXIgbXkgaGVhcnQs", b"WWV0IEkgbnVtYmVyIGhpbSBpbiB0aGUgc29uZzs=", b"SGUsIHRvbywgaGFzIHJlc2lnbmVkIGhpcyBwYXJ0", b"SW4gdGhlIGNhc3VhbCBjb21lZHk7", b"SGUsIHRvbywgaGFzIGJlZW4gY2hhbmdlZCBpbiBoaXMgdHVybiw=", b"VHJhbnNmb3JtZWQgdXR0ZXJseTo=", b"QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4="]
encoded_ciphertexts = [
    b"VKILfSeTcTdUNWC5q5xOGZypYj06VX80whYz5nRyPRrM3e5dJ+gPn+z/a+pRMdiIAV6veDoAAuB9r7skOpfqs7xWR3jFUFdAhcSqP8FTV3HfqjDK8s/MnCvfwtwzTkcFIv0PkwYnz4yKOKLHADKnzEZqSLobCj/8aMzgUZbbU9g=",
    b"UvpdeSWWe2QGZWbl+J9LHcr7Zz4/UC8wyEBtsXB0ZkiZ3eAPJr8Hm76tPu4GYoOMVF/6LToFBeEv/rtxapXq6roFFX/DAltNgpGuP8RWViTf+GfK8c+cmHnflosxGEYCeKYPnwInzYDfa6TFBjT2z0Q/HugYCW6oa526VpKKWt4=",
    b"DvBeKiOZezcHMTPkq58bHJz4NGU4Vnw0lUc5t3R9PEjP2+NTIroAn7iobOtcMY6JUlSrdzEJBeAsqOsna5XpsrwCQHySBFdMgZP1bZYGBiOE+zGeoMqQm3zZwNk/GxUDeapex1IgzNCNaKTHBzX6mRI9GO8eXG6tbcq2VpbWUdw=",
    b"VPIIdnSTK2IANzfpqZtPE5z5Ym01Ai5klUI9tnJ1Zk6UieZTd70Gk+uoOLsDNIvfVwOoeTsIVLUprb52YMC8suYHQCjEUVlNhsX5NcJTV3HX/TifoMzNmy+Jldw0HUNQdP5ew1YlnISNbqCUVGGgxkJtRbtLWDusOZ/jU5aMWt0=",
    b"UKINdyfEcTkBbDDs+ZoeGJasYWxoUH80wkdqs3YlZx7L3LNcK+oAzu2tO7gDYYiPVFOgfW0JWLMupLEhapvt7e8BQHqQVlcWhZX+NMdTVyKBqjSeo8qfyyPaxd81SEZSIvpfkQV1yYaEOKCWUDLyzE5rROpMCDz/b8nmA5GOAI4=",
    b"VPMMfiCVcDcGN2C8pc8eHZv4Y2s4V3o0xRM+sHNwZxqa2rBTJuoHne+rae1XMYiIW1f6Kz8IVeV/rbkhPpq67usBECmQAwxGhMT5bpRQCyGF+GTJ9ZubynmKxdplShABcK9cwA4nnNbeOfOSVGKhnhJrHu9JWm76PMjmUpXZVY8=",
    b"BPULKXfDfDhaYjTpqcdMSs2uZz8/ASFgxRNttHJwP0rLjbVdIb1QnuipPutVMonbUFavKGkJWbQo+LojasHn6r8AFSHFUQ9N0cGpapMAVCrSqzee9czNz3/YwIw3HURQcf5bkAd3zYzebPWTVmX7mUE8HupODWioMZ/nCZeMVNk=",
    b"BfUKeCuQcGFQbWburM0VGs/9YW1pUCs2l0Vo6yclZxuai+BaK+tXz+2pY79SNN7ZUAOtejsEU+Usr+txOpHu6rxVG3yTB1gR1ZKtb8cGACKBrDPOoMmfzivewNkxExcAdftcxQ93y4WIZPXAUWH2mUFuGLxJDT7+PcSzCMCLVdI=",
    b"B/FafyGSezYDYmHl/5sUSJiobj9oBnw0xBZo5CdzZx6d2rcKcuoPzu+qbr8EMoOPBlP9fW1QWeUqrewmO5q/v7oERinCXgtBgJH4asQDBHeB+DLM9pudn3zex4pkEhMOd/4OngBwwIWMPKDAAGOgxkI8TOxIWDj2apnmUZHdANI=",
    b"AqYBfCuUKzQGZj3qq5wVHJr8NG08Uitnk0Y953x9PBqd3+cKIroHmLj+Y7wGZNmPWlb+L20JVbd4qr11b5e/7uYBEiDEUlcTg8X4PsRQVCGF/znPp8qfmXnYwt0wGUAHdq4KwFQiwITbZf7GAmH1yxNoTrYfD2qqP5rkB5aOUNM=",
    b"U/ILKnTDcDlTNTy/+8oZScyvYjhtCy5ilRBp5XZxbBidiO5fJuEDyer6POxSYI+PUVevfm0BUO59+7p2a8DmvrgDF3+YUA1G18H6OMIDBCvQ8TGb9sPMxC3ex45gHhYFdv1fwgclnIGMZfXFUTf1xxRnSrgdXW3+aM+zVMTaAdw=",
    b"BqdcfHeVeDJUYDe+pMlOSp2rYWg7VSBgxkRu4XNwOE7J2OFYdeAEk7ujaO0GYImMUQT9d2wGWLd6+b90PMbm7ekFECqVBwhF0JX5P5EBACTQ8DaYo8LMzCLakIpiTkcGIPpclgV1wNTfPPbHUDTzyUE6G+1IDzuoOM22VcfdBNM=",
    b"VfQILSfELTkHNmO/q5gYGsr9bzg4Aiozk0U65XQnZ0ifieFeI7gBkrypPO5VZoKNBFCteD0JBuYtrLhyYJPuu+sBRy+XUF0WgJSvNZRVAnDXrDjJpMqey3zakNs/HkEHd6YKxQUgyIfePqOSV2fxz0RnT7kcXW79Pcq7BcTYBog=",
    b"B6VdKXaYL2ZSZDW4rpgYHp/8YmxoUno5whQ5t3J3Px2bgO4JJuEDy7n5a+5UNYiLAwOuKj0HULd8+7wla5Ds6eoEQ3jGVVlA0pGoPJZQViaErWXJ9s/MyiOLxtY1GxZTIvxclgYlm9CEavDIVTLwyBZuRLlPCWyqMM61UcHcANg=",
    b"APdeLHGWLzYANzK8pc8YG5r8NGhoUSwwl0I7tHAmO02V3ONacOgFyLusPOpXYt7cUgegezoDA+8qq7wmO5W7v+YEQSrGV1kXgZioPJRQC3ODrTGerJudyXvbwdtgSBNSJawNn1JyzI3fPKLIBzD2nUBuSu9ODjz6PZ23VsfaUd0=",
    b"UvcIeyeVcGZUZDe4/JwbTcr7Zm5tUC43yUJvsycmOE3M3bJaIO8Fmrqob7tcZYvbUl+vL24CWeYu+LFzPZPpvbwBRnuSXltEgcb+acVVAnDerTHJ8pjIyCvcl4o+SRNVd/pUwlEmwdHfbqfIBTT6m0FuH+sZXGP5ap+7VczeBok=",
    b"A/Ndf3bDfTRXYWe+/89ITpb9NzhuCi0zlUM+4SdyPBzI2+dcceoHzr+rabxVYY3bA1GvKD4BBuAu+74vPsbp7+4CFCzDBFpNhZf0P5NXC3GCqDPMpMmYznnWk4k2TRtSdaYJkAN2zoKObfbFVzSlnkZqSbZJCzj2O8qxAM3eWt8=",
    b"D/MPKiCVK2FTY2C/rpgYSZb4ZD9oB3gyk0MzsHBzahvJ3eVcduhTnLqsab0GYdneAQShKjADUu8t/Ll0PcTou+xVFiGTUAsThMT9b8JTCiGB/GTM8M2RnyPckIw+E0RVca4JklR2wYCIb6SWBWGhz0E4SbhJW22rPp+3CMfeB4k=",
    b"VKANeyWXfDAAbTfqpMlLEpv4NG86AigzkhEysCAga0/J3bBcd+kOnLuqb+8BYIncU1CvL2xQWO8nqOl2apa/sr9TEC2WV14XgJatOs0HUSLVrWDPoMudzH+Kkd4wHBJXJP5dlVJ3zoGLZPbJXTf3y0JtG70eCzmsO8+7VJbaBoo=",
    b"AaBZeXeULWNQYGfo/MceT8/7NT85VSFiyUMy4XMnaEnIjOYOJ+pTm776a78BNdmJA1eqKD4JU7N8qe11apbru71VFC2ZBQpM1Zf9PsQEV3HfqDme8MKenHzalto+TUcDJf0NngVyyNOOaafJUWX3zhE6T7kcDWuqaMqzU5eNBIk=",
    b"BaABdiKZKGYHNzforssZT5v4ZzhtViswxEs7sCZ2aEmegbJeIL8Em76oOOYBY97eUQP9KzxSUOIp+L92OpO9urtVGnuYU19FgMX/bpBSUHPR+DKfp8vLny+MnYw1HRAHdfsPn1EizNSJb6CUUzfxmRM8RboVC2ysap23U8DbAdk=",
    b"BPcLKSuVcDcGMmO4+5gUHJioYWRvUC44lEU4tHx3PB6Vi+ZTKrtTybz9bOpUNoneB1X6fjtXWLQs/O0hPZrvvb8BF33GUl4RhsP0ac1XC3CE/mWbpp7KniOJxt0zSkAFdK5ckQYiwY2JaPWUVDT7nk9pSbYdWDn/O5qyU8XXWtI=",
    b"U6FaLHTFKmIAbTLrqMoeG5qrZT1pVikzw0o54XIhPRjJgOINcukDk7r+O+8AM4KPUVD+LTtUUrQn+L51aJPrv+hTG3zFUFxAhpCoNJMDASKD+mWbrZ/Nnizakd4xSENXdqoIxVUlnNGOaP6VVWeixhI9SOoaXT6oMcWzAZbfAds=",
    b"APoIeyGXfzlQMDztr51LT5z+Zmw5UX1gwEQ94XUgZh+bjeJTKuBTnbH/Oe4EZIKEBgeuKmtQU7V8pO4uO5K9771TG33EU11G0cP5NcRVAHaE8DHMoc+bzymLwtgxHBQBc6xenlQqyYGEbvPEADPxzE44SbZOC2KoOZ2zVMDbA90=",
    b"APAId3aYLzYDY2a+/sdLHJmoYm1uViwywkNq53YnaR3OibQJIeFTyev/buhTadiEVFb8eDhVBOMuqOxxPMfn77pTFXiTVg0RgZaubsZVCiLW+WPOrMuQyyPWwI5kShVVIPoOkQ4imtOLPPLBUWX1z0I4GLsbWmuobc/mBZCJVto=",
    b"AqAJeXHGLDZbYza8/89ISp31Y241AX1jlRY5s3YlOhyUj+Ffdr1VmO2oar9SYNuNVQD8fzAABuMn/LAlaMC6779URyjBXgxDhZH7bsUEAHCB+jScrJnKzSjXk95jT0RTIqdckgImz4HfOPXEV2elyEJuG+0dCG/5b8qxAsHYAY0=",
    b"UKFdfHaQKjdUNTXsqccUSZr5b2w+UC4zxxA85HV8P0/MjrJccukOmOurYudQNo/eUVT8LT4BVu8nrbslO5Xn7usBQXrCUVlEh5P7b8FVUHfS/WSZpsjKnC3blo0xHRdTefpbk1V2mdPYbaSWB2SiykZpRbscXW7/OZjhBpWLVtM=",
    b"AvIIeCeSKzkEYmO4+84eHs2uNG5uBy84kxFo5nN3OhvJjeUOKupXm7mjae1XMtmMBwSrfDgJVOcs+b0uYcC8v+oAGnzFB1hNhMP6NZNcBCCD/jfKpM6YzXjfkotjSkdXIqhbkwArzICPO/GTVmL2yxFtTL4dWmr/Pp26AMaNVY4=",
    b"AqcOeSuYKjEHYmfvrs5OHsirbmw1ACxjkkA9sHN2bEmajeVfK+5Umrz5aroEY4OFBlKvfz5QBOIt+L8lbcHvvLsPQCmSBQ0U0cP+b8BcAXDSrWXEoc6ezCPel9cwSkcDIPsIkQJywI2KbqTDVWDxm05rSbpPCT+saMS1A5XeVds=",
    b"D6AOKyWZfDJVYTDprMtOGZirMG9vBn1iwhFo4yEhbBSc2+NdcOEDnrv4YuhUad+MBlOpfTtQVO8tpb9zYcDsvbpSQ3uTAl4RgpT8NMFcUyrTqmDF8Muanynbx4xnGBAPIPlangArmdePaqLFVGOgnBQ9GboaDTj9aMvhBcKMUIo=",
    b"D/cBfCCXcGUBNWbt+MpLE5r8bzg9Bno1lxY76yBxPUmVi+ZbI7gEkrCvae1VYYLZUF+tezwCAuB4/7Anb5Lqv+8GR3rDVV9ChpT5PMQGBSvV8GXEp5/My3+Jko0zEkQPIqsJxQN1z9fbbqSTUzD3z0c7Ge0eDm75aM62CcfdBog=",
    b"UPJdLHCTfmMBYDC5+MlPHsv1Z2o1Ai5jwUY5tHZxZkmejrQPK+hTk7z6bu1QYo2PUQWpeTpVUuYupL0jaZq6s+xSEXqQU1ZGi5n9PpddCiLWrzWbpJ6bzC/WktZlGxMOeapcnw8lwNOPa/HDUTOnmxRrT7ceBmL+bJqyUcCMUt0=",
    b"VKIAKSLEejlRY2G5/JgfHpyoYm1pCyBgwBQysyFxbE6Vibdcdu4Fnr6ubutVaYLfBgP5LDtVULd/pLhyYJTr770DEiyWA1kRhZmuP5RTACGBqzDE9p/Lz37Wwo00ExYGeaYJkA8rnoyEO/CRAjfyzEY8TOxPCjj+PM+zB8DdVt0=",
    b"AfFZLnTDcTYHMGHt/8caSpivMmppASFnxkBo5SV0PRnOgeRZKuoFzrqtY+dRYN6NU1D9KDgCVLd/qr0iPMC86u5SRnuQB1pF0ZeuaJdTC3GEq2TFp5yQyivfldhlHxoGcq9dxVMjy4KPZf6TVjf0zEJvH+tMCmmrPMq7ApDdA9g=",
    b"U6JZeSCVKDZTYjy4qcwbGJr+NG87Ays4w0Zo5X13Z0nMjOZTcegByLCqYuYAYo2MBlT8f2tSUrQrqe50aJPvu+dRFynFV1oUipT+OcVdCnSF/mDPrc7Lmy/bx9ZjGBEFcKgJkAd1nNaEPqTFXGWhxk46GO0cDG6saMqyUcWOAN4=",
    b"VaUBKnfCLDhUZjW4q80YTZr/bzpqBSo4wxRu5CAmbR7I2LAOJ+BTmOioO7tdZ47ZBwCtem4GV7cmpbp2PZe/7esAF3jBVgtNg8X+PZEGUCfT+jWcrcOemSyOlopgHxMEd/0OxVNwyYHYbfHEXDLyy0RmHLobD2+tOcjkAM3fUto=",
    b"BvAMKiWWLWVbYDDv/JwZE82pZzg+Ai8wlEM96iJzZxWe27BeIrtXnb6tOepcMtuLUgChLTBVVuMrr+1yOpHss+kCQHqXXwoWh5H+apEGCyLTq2TOp5iez3nXwtkzThcDIKlbkQV3ztbZaPLCVDP7xhQ7Tb4YCjv+OM6yBsGOVNI=",
    b"VPcIKyKTejhUMmfl+5oaT837NT01UC9nyRY96nQgOE+YgbJdI79SnOz6bewGZonbV1GrLWsEArB8/7gubpvrvOoBQyGUXw1MgpX9O5ZXASeErWeY9ZnIyX/Yl9s0GxpQcKdYxFQjwNTcOPbGU2/0yENmRLYVW2P7MM66VszfANo=",
    b"B6IMeHeXfWVSMTO8+cwdE838bzlqUS0zkkJttyIgO0iZirBbJLsGmb76ab1QZYjcBlasL20JAucoqrwmb8frve8FFyyWUFpE0JCoasEBUyXQ/zXO8cqbynjfl99jHUdUIv1VlAEnnNHcZKPIADTwykVsRLsfXD+tPsmzVMeNW9k=",
    b"BKYBfHaUeDFTZDbu+8hOSpz6N2hpBSw5k0s65HwmOB+birRdIrgDz7ytauxVYIOPAVH7K2sHWeMrrbshYJrq7+lWEnvFBF1Nipn1aMNVUXPVrWPMocjPzyrYlN4+GhtXcalUxVUinYTfOP7CAWLynk87SLweXWP4Pcm0UcSOUtg=",
    b"DvJcLCTDfGZRNmHlrMsZSc/9Z2RuByA1xBM94SUmaU2ZjrMIIesGyLGiaelVMtjZVQOheD5VA+Yu+L8hPZC67uoEQ32QBAxB0Jb9OJFUASXe+TDIpp/InCzfnIk/ExRXIKdelgYqyIXfbPSTXDShzRRrGe8fXTn5bc22AsLcUto=",
    b"AaEOLnaXcGJRYDO7/8gUHp//YWk/Byo4xUpu43cnb06Z3LQIcuEEy7yvb+wEZtmIBleteDAFU+Ep+7gubsG/suwAFymWB1xG0pj4O5BTVyLT/zHLpcmQxCzclY03HURVc6dellQrmoXYbfSUVDOix0A/HLtMDGr9aMu1U8aOVY4=",
    b"AqJdLSCQeTAAbWG4qMYYE8j4M2lpA3s2lBZq53YibBme2rcNIuADkrv4bOkGMtjfVlOrLG0HWe4p+Ot0acC/7ewARi6VUFlF1pP1asJdAiffr2PM8ZjMmCmLldlkExFScPwOwlQrnIaLb/7GV2DwyEA8T7oYBj+vPJ7kAcaJBNk=",
    b"AfoKe3CXcDIAZWO8r84aE8j+NWxpVypnlxdutyZya0nJieNfJuxQk+39Pu5dMtiNAAT7fjADV+ErqLxza5ftvLhRQSuUUloTgMb8acYDAHTT8WDP8MOeyCnZxd1gTRYAcqlaxA4kntaLP/TEUzPxyhE/H75ICGP8Os2yUc2LU9M=",
    b"VfcNLiLBfjdWNmHupZhLT5r7ZWhvUiwzk0c96n13ahqVj+RTJeAHm7uqbL9XYt6FAF6tKm4DVuR7pel0PcPuvLgGGynFXwpBh5f8apEACyCC/zae95/PySzdxdcyEkQEdahdlVUgyYXeaP6RB2/6zRE8HLpPXDurMJ6yUseOWt0=",
    b"BfUOfSDDKDFVYmTr+ccUEsr+NW5uByhlwhc74nYlbhnPjeVfIboOk7mpPr0BaYKMVlOreTpSUrAu/Lh1YcPuu+0GRnqRUlxB1capNMdQVCvQ/GDL8cmQzSLXk9wzH0cPcawPkgEjnYbYbvHEAG/2nkRoHu1MDDn+PMTgCcKLVYo=",
    b"AqBdfiqQcTUGYTW8/s0YGZ76N29pAi82kBNtsHMnOE6Zi7cPcuEDn+iobekHMoneU1/9fmtSULd9qL1xaMbpub0PFCvEAwxDipivacIDBCrT+DCb8piQzCzbnNZlSRYDd6wPl1QnntfcPKTJB2OlmxJqS+pIB275PMuzA5eNWoo=",
    b"V6IPeXeZfjUGZjy4qZ0cH5n+Y2g7An9nkhc8sSdyOhvJjuBYI+pUk+utOexRNYuLBwetKm4IWO8uqLEkYMDnvupSECvCUFlEh5KvPJFUBiDerWLKpsidyyvfkd1gHxZUIPldkg8hyoWJO6CWXTWlnERnTrsdXDitOZ7nBpbbAI4=",
    b"B6EMfiLGezQDYD3upJoeH82pNW08BCAxxhBq5yJwZhSYjOFSdroEn76jOLpVZt6KBgT5Kj0EWeV7qewub5bqu7tVFyyZAg1FhpL1acdQUHDRqjDL9Z6QmXjalNw3TxsHIPpbxVYnyNSJZfDCBjT1xxZmT78VCTz2aJ3jBMHbANw=",
    b"UvpdeSWWe2QGZWbl+J9LHcr7Zz4/UC8wyEBtsXB0ZkiZ3eAPJr8Hm76tPu4GYoOMVF/6LToFBeEv/rtxapXq6roFFX/DAltNgpGuP8RWViTf+GfK8c+cmHnflosxGEYCeKYPnwInzYDfa6TFBjT2z0Q/HugYCW6oa526VpKKWt4=",
    b"UvIBfHCReWVbNmbl/5pJScqvZmlpAi8ywEc6t3dzOkiUi+AOIb0AkrivPLgENdneB1WqfGwFBuMmrLB0b8bq6u1WQXuVVlxGh5iobpddB3DT8DnJrMnMziralYs/T0FQJKkPkgUnz4yPO6fDVG72nERrHugfBmj+MMq0Vc3YV4k=",
    b"VKcMLSGZKzNVNzTu/M1ISM/7YmpoCntgkkM6t3MgbU2e3eddJLwGz7r5YrhSMYKFA1KueWlTVeMurrpyOZfs6bxSFCuWXlpB0caubscAC3GCqmPE8cqZySLcwIswTxsEcKlckgV2noSEOPDCVDDyzUY4GLhJCDytP5mzB8zXW40=",
    b"D6AILCXBLTRSbWe8+84bHpf9Yj00VS1nl0c74CJ2ZkrIgLMKcuFUzrmjb79UaIiPA1L5Kz9UVOcoqet2OcPquOxTFC3CU1cWhcL4PsFWVyfSrGDMrM3LzCnXko4/ShNXJP0PnwIhy4eOafXJBzWlzRFpTbgYXDirMMS1VpHYB48=",
    b"BvZcLXGXKjZXNzblqMcfHpusNWRuBnwzlBQ7tHUnbBSVjeIKIuhUk7CpObwBZ9yEUAWqfD1QAuUvq7F1O5K97eYCEi3FU1tB15GuaMRVACHWrGSY8subyi+KkYo2SkNSdKoPwlN1mYKJPPXFATDxyxM/H+1IC2yob5+xVMzfW90=",
    b"APZZf3fGfTUGMjDtpJ9JGs2rZm05AyhjwxM6sHV2PU+f37QKcOlQmrn6ae8ENYzbUQL8LTsHUeUnq7EibZDvvbhVEXiUAlZB1pH0aJZUAiTSrWebp8uYmCnWkNw+HBpUIq8OwlUrmYONPqeVAjLxmRU6HrhPDDv5PMvjA8bfVok=",
    b"BqBbdnaRLGFabWHp/8ccHcqvZ25vBSg1yRRo631xaR/LiuZbcOEDybCjOeldMtvcWgP5eDpQULd7+75yPJTm6utREHiVUVsW1sX7NcVUBnPW/DLJpJiemSPckN5gHUABI/kJlgErzoHYOfPDXGSixxVrRbdJWm6qPcyzU5LXVds=",
    b"D/ENKSaTKjMBMmfkqMhPScv+NWptUiExw0Fps3MlOhnO37dZIr0Hmr2qYugDNtzeVF/9eT4JBeMrpLwnPJvovu1VE3rEVVgT0cH6PcEDUHPVrDDFoM7PyS7ckotnGRJQeaxbkwdwztDebKKSV2P1mxZvSLobB2usbZi1AZXWANo=",
    b"B/UKenHEKzdXMDfo+cdLHZf0MDg+BC44l0Y/4n1xPBrIiuRbJO8BzL+rbLhVaY/YAFH9KmlTVeMmrO0uPZHqv+9WRnvCVgpDgZj0P8cDBXaE/TTKoJueynvcnN0/HBFVJK1enwYimoLYaaKWVjf6m0U9S7ceBmj4a57mAcbaAIg=",
    b"AaIBLSDBejVSbTC5/ppLTsqrMjo8Vn85wEI443QmahyU3OVTcOAEyburObwBZYuNWl79Lz1UVLR9qbAga8C66r1RR3uSXwhEh8L7ascAViLU+mXFo5zImSrflNwwT0MOcvtZxQIqz9SKOPHEVm+hnEBuHutODW32bZ62VJHZA90=",
    b"D/cBfiWSeDBaMTzlq8gfSZr0ZGw1US05kko/5HEgax2Zie5bIOoPn76oO+8DNd+FVwegKDxSA+Inqr91bZq97uwCQH3DA1YQ1pj8b8NUU3He+WWfo8ucxCLdl9k1TkRUdvpYxQ4lmYKIPvfAXGD0nEVrSbpLDG2va5+7VcTXU4g=",
    b"D6ZaenCZfDRXYza4pMlOTs/6YGQ1UC80l0pttnUgZk+ci7VeIrtSmLGrO79cNo3fUQP6d2tXArQt/r8vaJHr6O5RF3jFBA1Hi5P0NJdVAnSDrzbNpZyZmCnZktgwG0dTJ6kIwgQmnNSJavKVXGL2yk49HLxMCTz4aM7jVMbeUN0=",
    b"AvVaeSOVfTcGN2e5rpoVGZj0NDltUC40yUA44yF9OBrOj7dbcO8AnbiibOdTZN6EBF6ve21VVecr/ukhO8S8vuxWFCzDAl0U0ZD/OZMGUSrUqDjIoMmaySPdl45gG0YPI/5fngYly4bZafPHXWahx0I4H+8dXzz+Os/kAM2NV9I=",
    b"B/VceyKXfWVTNTS7rcYcHp31N2w1USExwEcz5CAlaBSViLNeJ+5Sz++iabtTZInYVgT5LT0AWeN6pO1xaZa76LwDF32WVVgTgJSvO5YBAyTR/THF8J+fnnjdwYs/ExVScvpZlQUiytCOPKLBVjf2xkA9HO0ZBz/7a8q2Ac3YA4k=",
    b"D6ZaeCqVeGVWNmfk+cobTZj8ZGo7ASoykkRusyEiaUifgO9dcbgEzOyrPLsHadnYA1KofGpSUON8qL1ybJXru7xVFCDBUQxEhZmuP8QGAXberWXO982bmCPdwNs0TUAFIvpZk1QhmoKNaffCVmShxxJtT7YZDGz4MZq7CcGMU9g=",
    b"DvINdivFKjdVNWboqs9IHMqrNWQ6AC0wxRBu5nxzbkrJ2LcKcLoFnuj4Y+lVNdmKBlP5dzlSUeAu/Ox0OZG8v+cOFCnEX1YQgJGpP8RSVCffr2eb8MiazHyNxd0/HRdVIKdcnwd2wNbZPKTBVGbzzxFoGL1IBjmrOZ7nVsTdAIo=",
    b"BPVde3SQKGUBYmS/q8wUG8j8Y280Cy0xwEYyt3UnO0nJgeIOcOwPnbCoO+xcYN/cUlP6dzEIBbUprr50Ppvqs+wPRynDUQxEhsb+b8QEASrf8TTJrJufyXiMk4pnTkFQdPoIxQIkzNSIPPOUVWXzmU9uG+saCTn5PZ/hVseOA48=",
    b"APEOeCLEeGVTMWC8rchPHc30YWlpAitjkkpq43J1bR3Pi+FTde9Snev4OLtVYY3fVFP+dj0FA+Mmqb8hOsO86uYBQSuQXlwXgZX1apFVUSPU+DHEp8/LzizawIwyG0QAcaZVkQZxzo2MbaTAUmOmykVmH75PCGr/OMXnBs2JVNo=",
    b"BKUNKXCSKDRUbWTkrMZME5quZz04BS5lxUJu5iclbB6YibBacb1Xy+yvb71cYoLZVFeuKz0ABeN6qrtzOpW6vugDFSnFAAhDgZb+PcQABSPX+TnOrc+emCmNkN9kHUNVdKoOkw93zYSObaPAVjOnnEM/Hu0cWGmqMM3kBcffUIo=",
    b"V6EOLibCfzADYDPspcocEpv0Yz86VyBjxBFqtnwgOxvP3O9YcOFTyL//ae5RNo+LVgX5fGpQBLB6r+xxbsfv7egFRivEBAsR0sL7bpcDBCCC/WPMpZmZzX7cxo4zTxpSdapZnwN1m4PeZKCUUjOhnU5uGO8YWz/6OpnkAcLaAdw=",
    b"DqcMLiCUL2JQYWPlr8lPGJyrMGs6Vi4wx0A5tH0hOxucgOcKJL0DnrqvP7hUY4neUVSoejBQUbd9+Lsva5S97e4GFizCBVpCgcaqbZFWBiHWqDLOoM6cxSjXkN00SRAFd6kIxwAnnIeLaaKTBjTyzRRoGLkbD2P5O8WzUs2MBt4=",
    b"A/ZZeieWeWZRY2HorphOSpypMmhoVigxwkBptid3Ox3PjbdZJOsBybz4O7hSYN6FUgf8eWtTU+Z4qrkiOcS/7bsDEyzCVQsX18H/b8JVVnPf+znLo8mdmC/bxdZjShpQca0JkAN1mYSMPPHCV2TymkRoSr5PDW+vbZjgVseMBIo=",
    b"BfddfnTEfzhQZGa4rJsaEsivNDhtUnwylxE84nwmaB+Z2LRad+ABnLz4aO9QMo3eBl6gKjxSULUpqLhyYJW8s70GRi2XXgxDgpH+aMxQU3fQq2XMos/PxHzYl4s3HRcEd6wJwAB1m9DYbvPHBmL7nEE8Hr9LCDj7MM3kCcCOANM=",
    b"AvJad3OQfWQBNj2+r8saEpn/Zmg7V3s2wkcysCZxahjPiOMJdrhXnLv+aecDMYuLA1Ktdj9VArcuquogPMS96rgARCuTVVpHipb9acYDCyDQq2WZ8s6Qy3iNkd9jHBEAeKhZww8hzYzeZKfJXWannUJsSLsVCzutPJm0UpHbUtk=",
    b"APJbeCDGfmRWYGbu/8ZJGMuuNGVuVSE1k0I743cibRjLiOZTJO1UzOura+hWY9iKUACoLDwJArQq/rhxPcDvuroOGivCAlgU0saqacMHVHPQ/DHJp5jInCiKnN81HUQOJ/ldlw4jzoDbb/XBV2T7mUQ9H7wUWG2oa8W1A8SLW44=",
    b"D/FdfSqTe2NVbWG7qZ0YHp78MmVvUSs2lBZv5iZ3axWUi7MJI7wBzr/4YudXY4yPAFSgKz9SUOYo+bEnaJPrsr9VRiGZBFxMipaqPMRWVCfWrDmZ956YzHyJwd5lGhUPd/lckVUqyYCPa/fCAWLzzUM4Re8fCW79bZjnApHeWo8=",
    b"B6AJeybGfzUHYzS/q88UT5usYmk1UCE4xkY8tnB8aBWc2+YNJ+lSnrGpOO1dMtuMUAP7fDlTBuQprep0YJq/vuYOQSqXAF5Fg5D6NMQDC3DUr2DMpc3KnHncwt5lGxQFJKddn1Nym4KLPvHAUWX7nRVqSbtICWmoPMvhCMTZWtk=",
    b"UPUALiaRLDBbbGa7qptOSZb0ZGg6Byxjlxc44XF9ah3P3LRbJeFTnev+OL8DYNjfA1SuezwIA+YopLsibpK67e4PQXjDA1hM18WubpZQC3TRrTOYp8rIzijXkdg2T0EFcq4Pl1JwytOEZP6RUGWgm0dtSb5PDmL+P8nmBMfeWoo=",
    b"V6ZZKiGXcGFUMT3oqskfE8v5Ym06Bys3xhRvsHMlbkmfjrRZI+xSnbysOb1UaYKEW1OgeGsJWbJ8/7olaZvtu7gGGiiTAl5H1cb1P5RTBCPf/Dif98uezSzawY5lH0YAJPsKlVQgwNSNbvKVUmT7zBZmSbkYCj77O8WzB5HaANs=",
    b"DqcKKiPEfTUHYDK8+J9ISs+pYj81AyFgl0du5HImb0rP3O5cJO8Gk+/4Pu1UNYPbUlH6LTtUUucu+bAmb8brsuwDRn2SVV5Gisb0b8xTUHGC/jLP9smdxC/ZwdxjEhRXeKgKkQVxwIOFaPaTXDWmz0Q9RLkYCm76McW7UsHfU4g=",
    b"D6UMeCCWLzVWMWDk/M9JGMipZW80AHtgwxM96nUhO02Ui7IId+gEz+35a+hVNtuKVlCtL2oEA+cprO4kb8O/6e5RGy+ZVg9N1ZX+Pc1cVCOE+zmcoZnNyiyKx4ljExAOcvxfnwNwwI2JPvfCVzT2nBNqH+sVDTv+MZ/hAcPWA9I=",
    b"DvJeLXSZezkDYjTkq5hMTp34YGhoAC01xEVp4iJ2OBuZiuJeJOEAzLD9Oe0EZ4yPUlWhKD0GBe56qb9xbcTm6ugGEHyWVw9Mhcb/P5AAAyTS/TDJ8J+ay3/YxY02TxAAcKpakAByz4OOa6eVUTL2xk88SO9LXGj7apm6B5ffAN8=",
    b"U/tdKyHCLDkGYzXs+c5OTpf0MGo5BHo3xRQ/4HVyaRnM3OYPJOtUzrz/a+lUYImNVVD+fzEGWbUs/OkuOsHquu0GQyqSUlxChpX/P5RVACbT+WTJoJ+exS2Oxdg2GBUBJPsJk1ErzITZPPTGV27wyRQ4H78VBmv6MZmzUcTfWt4=",
    b"AqYAfHTBcTEANTXvqM0YT8quYzg7VitnyBA9tyF1bhmY3bBZIr8Fmr/6P7sENIKNW1KqKzgAU7cmqOkgasTu6LwFEirCBV0UgcOuP8xRBSXR8TjLocycyyyLlY0wSBYHeP4IlgR2yNHba6eVU2/2zxRrRLgZXWr+as3nBcfWA9g=",
    b"U/dZKnaZemUBbGDtrcYZTsqsMzo8UHs4xUdqs3ElPU6VgeNcKutSz+isOe9UZdyLBgOhLzEHA+Ep+e4nO8PouukAFCiXVVYWhJapNcNQVCPfqGCb98mZmHmMxoo2T0NVIqYJxQYkwI3caqfBBjSgzxNoGOgYBzj3Mcy2B5ffW9I=",
    b"UPYBd3OZK2YGMDTqqs8dGcz6Y2Q5UH8zxhM76nQiZh3IgeJTcOwPz7GjOLpVZYiOVwerfTkIWO94/ukuPMe7v7gPFiiWBF8U0JSvaMBXVHaD/zKfopvMzHzcktZkEhpXc6xaxQYiy4aIafGUBzelnBNmTLoZDG/5a860Ac3eUN8=",
    b"AvoLdnaQeDVbbGbtr84bSJqrM2xuVS45xBNutiJ9bU/M2LVTIrwBnu34artSYtjYUlKtfzsCVrMsrrAjOZbnsukPGyqUVVwTi5X6b5NUACLQ/2CZo8qdmXuOlt9gHxQBef1dxQN1m4CIa/bCXWagyURtRLdOCm3+PsrmBMOLVtw=",
    b"VfNcenaQcGEDNWflrc0UHMr6Mjg4UCkxlBMy4CAnak2fjO8KduEDmez+OOYHZYmOUlKqKzEIWeMmrukjbJTp7uwAFX2QXllB1sL7OpZUByvfrDbOpsyYnCqKnN03GBEOJ69ZlQ8rmdaLaafGUjWmzUA4RbgdBz/5bJ3nA8eJVI8=",
    b"D6Jcf3aQeGRTYzPr/5wbG57/Yz5tAC0xwhcz53UgbxiUirdacLwEzLivOLoGNouJBlehdm4FAeIn+Lgva8TqvuoAQy/FUwhMipD0OMFRU3OD+TOZrJ6bziLcwo1lHBZXJ69el1QkndCKZPGVBWfwzUJqHrgbDmmqbMu0As3eANM=",
    b"VacJeHaZfzMDbDG5pc9OHsz+Zz07AiowxRA66nR0Oh2Ui+cIKr9SyOqua+ZRaYrZW1OpfjFXVeEqqbovPpTtuLsPEn2RVg9G0cGvNJdWAyTRqDLOoJyfyCvZlNk3GxECIvxexAFxy4XfPPCWVGSnzBI4RbcaXGn6MMu7VcTcAN0=",
    b"UvFcLSbFejQBYmbqqZgUTsv+ZT1oAC1kkhQ4sHd3axqVi+MOJ70Bzr6oO+gDZoqFUlaqK2oGWOQrr7skOZbmv+oFECGTUgwTg5X7NMMHCyDR/GfFppuamXnek4k1SUEBdf0Ox1EimYOFavDEB2L3yhM4TLYdXz6vOp3kCczbW4k=",
    b"UqdeeiCTcDFSYTe5/8kdSJqsMD09CiBgw0c6sXwlaxnIjOBdcbtTmu2vPOxTMomIUlOgejtQAeN7q7tybsHnvOhTF33GUwwX0sX1PsJcUSbT8GfNp8KZxHuNx9ZgGhFTdvsJxA91yYHfZfbEVmGizRJrHOoVXWytOsTmA5COU9I=",
    b"BPIBLHSRfzhTZGO/pc5MTsquYmk0A3wyxEQz53RzOhvMgLMIcOpXnOivY+9SYY/YAVD+f2wDBbN//LkkbpPuuLtVEyCRVg1D0ZT6PcAAVibfq2CfrJ/NyyrWkYkzSBoAcq1Ywg8qzdeJZPCTBjD6nEE/HO8UCzn4MJ3gBMDeA9k=",
    b"UvZceyCXLTNTZWfkqc5OEsz7NGg/AH1kkxQ/5nInP0qdjONcI7gGk7H5POgBZ42OWlH9LT4IBe8vr78lbpbqs+oPESnBXgwQhJj/PsFRCnSC/DOb9s+cyiyMlotgHRNSd/5aww53noKIP/WWADD2z0VtGLgYC2v6OsTmVMfeA9w=",
    b"BfBZdybGLzQAMGHtrMkfTZ/9N201C3s4kkVv5icnOBSY27NTIOEPyb2pbeoGYovfAVT5f2oBA7Mu/uwmbpbt6ekDFiiVUFoR0pj9P8NVC3HSqzXFrMPMzyyJwNk2GRICdq8JlA5wnIfbaqLDAmX3nUc9Sb0cCDn4bZ3hVsbYBNk=",
    b"U/BbLiSZKzFaNjLlpcgYSJb+YGw8BSFnwUI9s3xyaBqZ3+8PIr8Bme+sa+hdYY/bW1X8KG4FWeMtqL9ybpvvvOZVFSvCB15DgcH4OcwEASqF8THJ98ufyCPYk9c0SRZVcKwKkwMgyIeLbaTCB26myhM/GLtPCG+tMci3CcCKUY4=",
    b"VPVafiCWf2VVZTa8q8odSpqrYDg7USE1xEJp53AgPEiZjLVZK+4Cz+itaeoBNtmEAASsfWwEBeMu/OwhPcfuv+lVEH3GXllEgpOvbpMEAHDUqzGc8cOZxCuMx4pkGkAEdf0KnlIqzYyEO/XEBm/zxkZqTrZIBzmtaM6wAJKOVdM=",
    b"UqILe3eYe2UANzLs/p1OE5b9NWo/CnpnkxZqtH1wPB/MiecIIbsPkuqvP+tRNIPYUgP+fToEVrcvquonaca8ueYHRHqYUFxG0ZaoaccEBiaDrGDN9c/NyCnbwtg1EhMPdaxYnwMnnoOPbqSTVGX0mkRtTLgaC2/4Pp+0VsTaB44=",
    b"UvFdeSXGL2MAMjHlqM9PEp2sb245ASg0wUNt63cgPU7I37RaJuAEnO34aOxUZ9+LUgT+fDhTUbctqr4nbZXuveoBEiuZVFlNgMX5PJYAU3HRqmWYocjIziiKnIk1SBpUef5bkgJ1z9Pfb/bEVTOizk9tSugbCGP7bJjmCJLWVd4=",
    b"AqdbKiSSLzBVYDfsqZ0eE8/1YTg7UShlw0A74yVybByYjrBfJOBSmOioY78EZ43bAQX+fW4DUOV/qesvPZq7suoAGnuXUVZAhpCqapABVCCDr2fLpp+dyizalIwzHBAOcqdexwZyy9OJOaLJBWLzmhZuTe1MDGOobc23VJDcBt4=",
    b"BfNbfyWYKzkAZTbqqp8fGZn0Y2VtBnw3lEQy53Z2Px/Oje4PI+0BmbyuYu1TZ4LfVACsKzoEVrMtpb4hPpbrsr0AFS6ZUwtHh8OoOZBXVnaFqjXNpM2Rnivcko41SENQeKsJwFMjzYPZOfXCVWH1nBVvSOwUCG72P5/hVM2MV9I=",
]
ciphertexts = [b64decode(encoded_ciphertexts[i]) for i in range(len(encoded_ciphertexts))]

print("stats")
print(len(ciphertexts))  # 50 collected ciphertexts

longest_c = max(ciphertexts, key=len)  # longest ciphertext: 111 bytes
max_len = len(longest_c)
print(len(longest_c))

shortest_c = min(ciphertexts, key=len)  # shortest ciphertext: 33 bytes -> all ciphetexts have at least 33 bytes, so the first 33 bytes of the keystream will be the easier to guess since we have more statistical information!
min_len = len(shortest_c)
print(len(shortest_c))

#################################################
# guess the first byte: naive approach: count the ascii chars

#  counters = numpy.zeros(256, dtype=int)
#
#  for guessed_byte in range(256):
#      for c in ciphertexts:
#          # simulate decryption:
#          if chr(c[0] ^ guessed_byte) in ascii_letters:
#              # count the occurrences of each byte that, xored with the ciphertext, produces an ascii letter: candidate byte of the keystream
#              counters[
#                  guessed_byte] += 1  # The fundamental mistake in this approach is this, that each letter found has the same value, but actually each letter has a weight, that can correspond to how frequent that letter is in the plaintext language! If I find a w, it is less probable that the keystream was correct, since it is a rare letter, so it is more probable that it should be considered as a wrong character, while if I find an 'e', it is more likely that it is the right keystream!
#
#  max_matches = max(counters)
#  print(f"max_matches={max_matches}")
#
#  match_list = [(counters[i], i) for i in range(256)]
#  print(match_list)
#  ordered_match_list = sorted(match_list, reverse=True)
#  print(ordered_match_list)
#
#  candidates = []
#  for pair in ordered_match_list:
#      if pair[0] < max_matches * .95:
#          break
#      candidates.append(pair)
#
#  print(candidates)
#
#
# #################################################
# # guess the second byte: naive approach: count the ascii chars
#
# counters = numpy.zeros(256,dtype=int)
#
# for guessed_byte in range(256):
#     for c in ciphertexts:
#         if chr(c[1] ^ guessed_byte) in ascii_letters:
#             counters[guessed_byte] +=1
#
# max_matches = max(counters)
# print(max_matches)
#
# match_list = [(counters[i],i) for i in range(256)]
# # print(match_list)
# ordered_match_list = sorted(match_list, reverse=True)
# # print(ordered_match_list)
#
# candidates = []
# for pair in ordered_match_list:
#     if pair[0] < max_matches * .95:
#         break
#     candidates.append(pair)
#
# print(candidates)
#
#
#
# ##############################33
# # guess all the bytes
#
candidates_list = []
hexletters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for byte_to_guess in range(min_len):
    counters = numpy.zeros(256, dtype=int)

    for guessed_byte in range(256):
        for c in ciphertexts:
            if chr(c[byte_to_guess] ^ guessed_byte) in hexletters:
                counters[guessed_byte] += 1

    max_matches = max(counters)
    # print(max_matches)

    match_list = [(counters[i], i) for i in range(256)]
    # print(match_list)
    ordered_match_list = sorted(match_list, reverse=True)
    print(ordered_match_list)

    candidates = []
    for pair in ordered_match_list:
        if pair[0] < max_matches * .95:
            break
        candidates.append(pair)

    # print(candidates)
    candidates_list.append(candidates)

# for c in candidates_list:
#     print(c)


keystream = b''
for x in candidates_list:
    keystream += x[0][1].to_bytes(1,byteorder='big')

from Crypto.Util.strxor import strxor

digests=[]
for c in ciphertexts:
    digests.append(strxor(c[:min_len],keystream))
print(digests)

# Now do a dictionary attack on the digests.

##################################################
# approach with stats
#
# candidates_list = []
#
# for byte_to_guess in range(max_len):
#     freqs = numpy.zeros(256, dtype=float)
#
#     for guessed_byte in range(256):
#         for c in ciphertexts:
#             if byte_to_guess >= len(c):
#                 continue
#             if chr(c[byte_to_guess] ^ guessed_byte) in printable:
#                 freqs[guessed_byte] += CHARACTER_FREQ.get(chr(c[byte_to_guess] ^ guessed_byte).lower(), 0)
#
#     max_matches = max(freqs)
#     # print(max_matches)
#
#     match_list = [(freqs[i], i) for i in range(256)] # each byte i has this frequency of being a keystream byte
#     # print(match_list)
#     ordered_match_list = sorted(match_list, reverse=True)
#     # print(ordered_match_list)
#
#     # candidates = []
#     # for pair in ordered_match_list:
#     #     if pair[0] < max_matches * .95:
#     #         break
#     #     candidates.append(pair)
#
#     # print(candidates)
#     candidates_list.append(ordered_match_list)
#
# for c in candidates_list:
#     print(c)
#
#
# keystream = bytearray()
# for x in candidates_list:
#     keystream += x[0][1].to_bytes(1, byteorder='big') # we now take the most probable first candidate byte computed from each ciphertext, and create the most probable keystream, that will be used to xor all the ciphertexts 1 Byte at a time
#
# print(keystream)
# from Crypto.Util.strxor import strxor
#
# keystream[0] = 148 # Force keystream[0] from tailored information: Capital letters or seeing which words (expecially towards the end) needs to be corrected because the guessed keystream byte was wrong
#
# dec = keystream[1] ^ ciphertexts[0][1]
# dec2 = keystream[2] ^ ciphertexts[0][2]
#
# mask = dec ^ ord('h')
# keystream[1] = keystream[1] ^ mask
# mask2 = dec2 ^ ord('i')
# keystream[2] = keystream[2] ^ mask2
#
# print(keystream)
# for c in ciphertexts:
#     l = min(len(keystream), len(c))
#     print(strxor(c[:l], keystream[:l]))
