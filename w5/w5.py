#!/usr/bin/env python
# coding: utf-8

import gmpy2



P = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171

G = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568

H = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

def meet_in_the_middle(_p, _g, _h):
    B = gmpy2.mpz(pow(2,20))
    p = gmpy2.mpz(_p)
    g = gmpy2.mpz(_g)
    h = gmpy2.mpz(_h)
    lsb_candidates = {}
    for x in range(B):
        lsb_candidates[gmpy2.divm(h, gmpy2.powmod(g, x, p), p)] = x
    for x in range(B):
        msb = gmpy2.powmod(g, gmpy2.mul(B, x), p)
        if msb in lsb_candidates:
            return gmpy2.add(gmpy2.mul(B, x), lsb_candidates[msb])
    return 0

print(meet_in_the_middle(P, G, H))


# add(x, y) returns x + y. The type of the result is based on the types of the arguments.
# powmod(x, y, m) returns (x ** y) mod m. 
# divm(a, b, m) returns x such that b * x == a modulo m. 
# mul(x, y) returns x * y. 