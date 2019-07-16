using Parsers

function parseInt_parsers(num_str::AbstractString)
	return Parsers.parse(Int,num_str)
end

a = parseInt_parsers(readline())

@time for i = 1:a
	b,c = map(parseInt_parsers,split(readline()))
end
