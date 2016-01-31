PARAMS = {
	'keyWidth': 70,
	'tallHeight': 200,
	'roundingHeight': 50,
	'horizontalSpacing': 20,
	'verticalSpacing': 10,
	'borderHeight': 10,
	'borderWidth': 10,
}

TOP_ROW = 1
MIDDLE_ROW = 2
VOWEL_ROW = 3

KEYS = {
	's': {
		'x': 1,
		'y': TOP_ROW,
		'tall': True,
		'rounded': True,
	},

	't': {
		'x': 2,
		'y': TOP_ROW,
		'tall': False,
		'rounded': False,
	},

	'p': {
		'x': 3,
		'y': TOP_ROW,
		'tall': False,
		'rounded': False,
	},

	'h': {
		'x': 4,
		'y': TOP_ROW,
		'tall': False,
		'rounded': False,
	},

	'k': {
		'x': 2,
		'y': MIDDLE_ROW,
		'tall': False,
		'rounded': True,
	},

	'w': {
		'x': 3,
		'y': MIDDLE_ROW,
		'tall': False,
		'rounded': True,
	},

	'r': {
		'x': 4,
		'y': MIDDLE_ROW,
		'tall': False,
		'rounded': True,
	},

	'star': {
		'x': 5,
		'y': TOP_ROW,
		'tall': True,
		'rounded': True,
	},

	'f': {
		'x': 6,
		'y': TOP_ROW,
		'tall': False,
		'rounded': False,
	},

	'p2': {
		'x': 7,
		'y': TOP_ROW,
		'tall': False,
		'rounded': False,
	},

	'l': {
		'x': 8,
		'y': TOP_ROW,
		'tall': False,
		'rounded': False,
	},


	't2': {
		'x': 9,
		'y': TOP_ROW,
		'tall': False,
		'rounded': False,
	},

	'd': {
		'x': 10,
		'y': TOP_ROW,
		'tall': False,
		'rounded': False,
	},

	'r2': {
		'x': 6,
		'y': MIDDLE_ROW,
		'tall': False,
		'rounded': True,
	},

	'b': {
		'x': 7,
		'y': MIDDLE_ROW,
		'tall': False,
		'rounded': True,
	},

	'g': {
		'x': 8,
		'y': MIDDLE_ROW,
		'tall': False,
		'rounded': True,
	},


	's2': {
		'x': 9,
		'y': MIDDLE_ROW,
		'tall': False,
		'rounded': True,
	},

	'z': {
		'x': 10,
		'y': MIDDLE_ROW,
		'tall': False,
		'rounded': True,
	},

	'a': {
		'x': 3.5,
		'y': VOWEL_ROW,
		'tall': False,
		'rounded': True,
	},

	'o': {
		'x': 4.5,
		'y': VOWEL_ROW,
		'tall': False,
		'rounded': True,
	},

	'e': {
		'x': 5.5,
		'y': VOWEL_ROW,
		'tall': False,
		'rounded': True,
	},

	'u': {
		'x': 6.5,
		'y': VOWEL_ROW,
		'tall': False,
		'rounded': True,
	},

}

SVG = {
	'main': """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="%(boardWidth)d" height="%(boardHeight)d"
     xmlns="http://www.w3.org/2000/svg" version="1.1">
 <style type="text/css"><![CDATA[
     path { fill:#000; stroke: none; }
     rect { fill:#000; stroke: none; }
  ]]></style>

    %(contents)s
</svg>""",
	'groupStart': '<g id="%(key_id)s">',
	'groupEnd': '</g>\n\n',
	'bodyFilled': '<rect width="%(keyWidth)d" height="%(keyHeight)d" x="%(x)d" y="%(y)d" />',
	'bodyOpen': """
<rect width="%(keyWidth)d" height="%(borderHeight)d" x="%(x)d" y="%(y)d" />
<rect width="%(borderWidth)d" height="%(keyHeight)d" x="%(x)d" y="%(y)d" />
<rect width="%(borderWidth)d" height="%(keyHeight)d" x="%(rightBorder)d" y="%(y)d" />
""",
	'bodyOpenBottom': """
<rect width="%(keyWidth)d" height="%(borderHeight)d" x="%(x)d" y="%(bottomBorder)d" />
""",
	'roundingFilled' : '<path d="M%(x)d,%(bodyBottom)d s%(keyMiddle)d,%(roundingHeight)d %(keyWidth)d,0" />',
  	'roundingOpen' : """
<path d="M%(x)d,%(bodyBottom)d
c0,%(roundedOuterHeight)d %(keyWidth)d,%(roundedOuterHeight)d %(keyWidth)d,0
h%(minusBorderWidth)d 
c0,%(roundedInnerHeight)d %(minusInnerRoundingWidth)d,%(roundedInnerHeight)d %(minusInnerRoundingWidth)d,0" />
""",

}


def write_svg(filename, contents):
	out = file(filename, 'w')

	localParams = PARAMS
	localParams['contents'] = contents
	localParams['boardWidth'] = (PARAMS['keyWidth']+PARAMS['horizontalSpacing'])*10
	localParams['boardHeight'] = PARAMS['tallHeight']*1.8

	out.write(SVG['main'] % localParams)
	out.close()

def svg_for_key(key_id, isFilled):
	result = ''

	if isFilled:
		whetherFilled = 'Filled'
	else:
		whetherFilled = 'Open'

	details = KEYS[key_id]
	keyWidth = PARAMS['keyWidth']
	keyMiddle = keyWidth / 2
	roundingHeight = PARAMS['roundingHeight']
	borderHeight = PARAMS['borderHeight']
	borderWidth = PARAMS['borderHeight']

	xMultiplier = keyWidth + PARAMS['horizontalSpacing']
	x = xMultiplier * (details['x']-1)
	x += PARAMS['horizontalSpacing']/2

	if details['tall']:
		keyHeight = PARAMS['tallHeight']
	else:
		keyHeight = (PARAMS['tallHeight']-PARAMS['verticalSpacing'])/2

	if details['y']==TOP_ROW:
		y = 0
	elif details['y']==MIDDLE_ROW:
		y = PARAMS['tallHeight'] - keyHeight
	else:
		y = PARAMS['tallHeight'] + PARAMS['roundingHeight']/2

	bodyBottom = keyHeight+y
	rightBorder = (keyWidth - borderWidth)+x
	minusBorderWidth = -borderWidth
	minusKeyMiddle = -(keyMiddle-borderWidth)
	minusInnerRoundingWidth = -(keyWidth-borderWidth*2)
	roundedInnerHeight = roundingHeight - (borderHeight*3)
	roundedOuterHeight = roundingHeight - (borderHeight*2)
	bottomBorder = bodyBottom - borderHeight

	### now make the SVG

	result += SVG['groupStart'] % vars()
	result += SVG['body'+whetherFilled] % vars()

	if details['rounded']:
  		result += SVG['rounding'+whetherFilled] % vars()
	elif not isFilled:
		result += SVG['bodyOpenBottom'] % vars()

	result += SVG['groupEnd'] % vars()

	return result

def write_svg_for_named_keys(filename, keys, isFilled):

	contents = ''
	for key in sorted(keys):
		contents += svg_for_key(key, isFilled)

	write_svg(filename, contents)

def main():

	write_svg_for_named_keys('board.svg', KEYS.keys(), isFilled=False)

	for key in sorted(KEYS.keys()):
		write_svg_for_named_keys(key+'.svg', [key], isFilled=True)

if __name__=='__main__':
	main()

