function parseInt_default1(num_str::AbstractString)
	return parse(Int,num_str)
end

a = parseInt_default1(readline())

@time for i = 1:a
	b,c = map(parseInt_default1,split(readline()))
end
