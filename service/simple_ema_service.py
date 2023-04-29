import os

ITERATION = int(os.getenv('ITERATION'))

class SimpleEmaService:

    def getEma(candle, ema):
        price = candle
        alpha = 2 / (ITERATION + 1)
        return (alpha * price) + (1 - alpha) * ema

    def calculateSimpleEma(candles):
        innerCandles = candles
        prevEma = innerCandles.pop(0)
        for candle in innerCandles:
            prevEma = SimpleEmaService.getEma(candle, prevEma)
        return prevEma