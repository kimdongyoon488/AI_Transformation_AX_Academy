export class MyDate {

    constructor(year, month, day) {
      
      this.year = year;
      this.month = month;
      this.day = day;
      this.daysInMonth = [31, this.isLeapYear(year) ? 29 : 28, 31, 30, 
        31, 30, 31, 31, 30, 31, 30, 31]
    }
  
    getFormattedDate() {
        
        // 조건 1 : 년 데이터가 음수거나 0이면 1년으로 처리
        if(this.year <= 0){
            this.year = 1
        }

        // 조건 2: 월 데이터가 음수거나 0값이면 1월로 처리하고 월의 범위를 벗어나면 12월로 처리
        if(this.month <= 0 ){
            this.month = 1
        } else if(this.month > 12){
            this.month = 12
        }

        // 조건 3: 일 데이터가 음수거나 0값이면 1일로 처리하고 일의 범위를 벗어나면 마지막 일로 처리
        // (윤년일때는 2월은 29일까지 화면에 출력 가능하도록 처리)
        if(this.day <= 0 ){
            this.day = 1
        }else if(this.daysInMonth[(this.month - 1)] < this.day){
            this.day = this.daysInMonth[(this.month - 1)]
        }
        return `${this.year}년 ${this.month}월 ${this.day}일`;
    }
  
    isValid() {
      return !isNaN(this.date.getTime());
    }
  
    isLeapYear() {
      return (this.year % 4 === 0 && this.year % 100 !== 0) || this.year % 400 === 0;
    }
  }