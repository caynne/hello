# -*- coding:utf-8 -*-


getUser = '''declare @En_Date varchar(10)='2018-05-10',
		    @appid int ='100000058'
select count(distinct case when clienttype in ('0','1','2')  and convert(varchar(10),sm.addtime,23)=@En_Date then user_name else null end ) 当日APP新增注册用户数,
		   count(distinct case when clienttype in ('0','1','2') then user_name else null end) as 累计APP注册用户数, 
		   count(distinct case when isnull(sm.ClientType,'4') in('4','5') and convert(varchar(10),sm.addtime,23)=@En_Date then user_name else null end ) 当日H5新增注册用户数,
		   count(distinct case when  isnull(sm.ClientType,'4') in('4','5') then user_name else null end) as 累计H5注册用户数, 
		   count(distinct case when convert(varchar(10),sm.addtime,23)=@En_Date then user_name else null end )当日新增注册用户数,
		   count(distinct user_name) as 累计注册用户数 
from  hk_storemaster sm
where  not  exists  ( ----去除导入店主
			select user_name from vpclub_report.dbo.Import_Store_Mast b 
			where sm.user_name=b.user_name and sm.appid=b.appid )
			and convert(varchar(10),sm.addtime,23)<=@En_Date  
			and sm.appid=@appid

'''