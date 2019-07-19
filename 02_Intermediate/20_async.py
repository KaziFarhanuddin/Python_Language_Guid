import asyncio
# import aiohttp
# This is concurrency

async def find_divisibles(inrange, div_by):
	print(f"finding num in range {inrange} divisible by {div_by}")
	located = []
	for i in range(inrange):
		if i % div_by == 0:
			located.append(i)
		if i % 50000 == 0:
			await asyncio.sleep(0.00001)
	print(f"Done bw/ num in range {inrange} divisible by {div_by}")
	return located


async def main():
	divs1 = loop.create_task(find_divisibles(5080000, 34113))
	divs2 = loop.create_task(find_divisibles(100052, 3423))
	divs3 = loop.create_task(find_divisibles(500, 33))

	await asyncio.wait([divs1, divs2, divs3])
	return divs1, divs2, divs3

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	d1, d2, d3 = loop.run_until_complete(main())
	print(dir(d1))
	print(d1.result())
	loop.close()
