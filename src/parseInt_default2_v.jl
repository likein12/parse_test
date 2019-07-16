function parseInt_default2(num_str::AbstractString)
	ss = codeunits(num_str)

	x = 0
	for i = 1:length(ss)
		n = ss[i] - UInt8('0')
		x = 10x + n
	end
	return x
end

function readline_org()
	read = readline()
	return read[1:length(read)-1]
end

a = parseInt_default2(readline_org())

@time for i = 1:a
	b,c = map(parseInt_default2,split(readline_org()))
end


#parseInt_default2の部分についてはfrom:(@ sgryjp)
#この関数の場合、改行コードを取り除く必要があるので、readline_org()関数を使用
