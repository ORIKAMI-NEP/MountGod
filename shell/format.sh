# sh format.sh naroNovel
cat "data/$1.txt" |\
    perl -pe "s#[^ｦ-ﾟぁ-ゟァ-ー亜-腕弌-熙？]##g" |\
    perl -pe "s#\r\n#\n#g" |\
    perl -pe "s#(.*?(。|!|！|\?|？))#\1\n#g" |\
    perl -pe "s#^\n##g" > "data/data.txt"
cat "data/data.txt" |\
    perl -ne 'BEGIN{$p="";} chomp; if($.>1){print $p . "</s>" . $_ . "\n";} $p=$_;' > "data/data.train.txt"
head -n 3000 "data/data.train.txt" > "data/data.validation.txt"
head "data/data.validation.txt"
