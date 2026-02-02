def count_even_numbers(arr)
  count = 0
  arr.each do |x|
    count += 1 if x.even?
  end
  count  # 最後の式が返る
end