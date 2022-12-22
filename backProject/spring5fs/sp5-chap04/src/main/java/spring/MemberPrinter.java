package spring;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.lang.Nullable;

import java.time.format.DateTimeFormatter;
// import java.util.Optional;

public class MemberPrinter {
    // 1
    // @Autowired(required = false)

    // 2
    // @Autowired
    // private Optional<DateTimeFormatter> formatterOpt;

    // 3
    // @Autowired
    // @Nullable
    // private DateTimeFormatter dateTimeFormatter;

    private DateTimeFormatter dateTimeFormatter;

    public MemberPrinter(){
        dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy년 MM월 dd일");
    }

    public void print(Member member){

        // 2
        // DateTimeFormatter dateTimeFormatter = formatterOpt.orElse(null);

        if(dateTimeFormatter == null){
            System.out.printf("회원 정보: 아이디=%d, 이메일=%s, 이름=%s, 등록일=%tF\n", member.getId(), member.getEmail(), member.getName(), member.getRegisterDateTime());
        }else{
            System.out.printf("회원 정보: 아이디=%d, 이메일=%s, 이름=%s, 등록일=%s\n", member.getId(), member.getEmail(), member.getName(), dateTimeFormatter.format(member.getRegisterDateTime()));
        }
    }

    // 1
    // @Autowired(required = false)
    // public void setDaterFormatter(DateTimeFormatter dateTimeFormatter){
    //     this.dateTimeFormatter = dateTimeFormatter;
    // }
    
    // 2
    // @Autowired
    // public void setDaterFormatter(Optional<DateTimeFormatter> formatterOpt){
    //     if(formatterOpt.isPresent()){
    //         this.dateTimeFormatter = formatterOpt.get();
    //     }else{
    //         this.dateTimeFormatter = null;
    //     }
    // }

    // 3
    @Autowired
    public void setDaterFormatter(@Nullable DateTimeFormatter dateTimeFormatter){
        this.dateTimeFormatter = dateTimeFormatter;
    }
}