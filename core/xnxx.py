B
    �ĥ\f  �            	   @   s�  d dl Z d dlZd dlZd dlZd dlZyd dlZd dlZW n ek
rX   ed� Y nX g Z	g Z
g Zg Zyed�ZW n ek
r�   e�  Y nX ede� d�� yed�Zed�ZW n ek
r�   e�  Y nX e�d�s�de� �ZneZee� G d	d
� d
�ZG dd� de�Zeee�Ze��  e�� Ze�e� e�e�� � G dd� de�Zx�ee e��D ]zZ!yVedee! � d�� ed��"� Z#e#dk�r�ed� eee! e��$�  ed� n�wbW n ek
�r�   e�  Y nX �qbW dS )�    Nz"
! Please Install aiohttp asyncio
zSiapa Namamu? : z
      Nama Saya a9   
      Saya Suka Coly !
      
      Saya Bersumpah Di saat Memakai Tool ini
      Saya Menanggung dosa saya sendiri dan tidak Melibatkan Author
      - Sumpah Diri sendiri sebagai Manusia :v
      ()-----[ Xnxx-Dl ]-----()
        by : 407 Authentic Exploit
        codename : JaxBCD
        version : 0.3-crot
zQuery : zProxy : zhttp://c               @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�getPagec             C   s   || _ || _d| _d S )Nzhttps://www.xnxx.com)�q�p�x)�self�query�proxy� r	   �xx.py�__init__+   s    zgetPage.__init__c          
   �   sx   t jd| j� d| j� �| jd�4 I d H �@}|�� I d H }t�d|�}xtt	|��D ]}t
�|� qRW W d Q I d H R X d S )N�GETz/search/)r   z<li><a href="(.*?)">\d+<)�aiohttp�requestr   r   r   �text�re�findall�list�set�page_1�append)r   �res�contentZget_pager   r	   r	   r
   �getpage0   s
    *zgetPage.getpagec          
   �   s�   t jd| j� |� �| jd�4 I d H �z}|�� I d H }t�d|�}t�d|�}|t|�d  d � }x0tt|��D ] }t	�
|| � t�
|| � qpW |j W d Q I d H R X d S )Nr   )r   z<a href="(.*?)"><imgztitle=".*?">(.*?)</a></p><p�   )r   r   r   r   r   r   r   �len�range�page_2r   �titles�closed)r   Zcpr   Zctn�url�titleZurls�ir	   r	   r
   �getcontentpage8   s    &zgetPage.getcontentpagec             �   s&   � fdd�t D �}tj|� I d H  d S )Nc                s   g | ]}� � |��qS r	   )r"   )�.0r   )r   r	   r
   �
<listcomp>E   s    z2getPage.start_get_content_page.<locals>.<listcomp>)r   �asyncio�gather)r   Ztkr	   )r   r
   �start_get_content_pageD   s    zgetPage.start_get_content_pageN)�__name__�
__module__�__qualname__r   r   r"   r'   r	   r	   r	   r
   r   )   s   r   c                   s8   e Zd Z� fdd�Z� fdd�Zdd� Zdd� Z�  ZS )	�getlinkc                s   t � �||� t�� | _d S )N)�superr   r%   Zget_event_loop�loop)r   r   r   )�	__class__r	   r
   r   J   s    zgetlink.__init__c                s&   t �t� �� � | j�t� �� � d S )N)r%   �runr,   r   r-   �run_until_completer'   )r   )r.   r	   r
   �_fetch1O   s    zgetlink._fetch1c          
   �   sh   t jd| j� |� �| jd�4 I d H �4}|�� I d H }t�d|�}t�|d � |j	 W d Q I d H R X d S )Nr   )r   z<a href="(.*?)"><imgr   )
r   r   r   r   r   r   r   �linkr   r   )r   r   Zrespr   Zlnkr	   r	   r
   �getlinksT   s
    &zgetlink.getlinksc             �   s&   � fdd�t D �}tj|� I d H  d S )Nc                s   g | ]}� � |��qS r	   )r3   )r#   r   )r   r	   r
   r$   \   s    z"getlink.fetch2.<locals>.<listcomp>)r   r%   r&   )r   Ztaskr	   )r   r
   �fetch2[   s    zgetlink.fetch2)r(   r)   r*   r   r1   r3   r4   �__classcell__r	   r	   )r.   r
   r+   I   s   r+   c               @   s   e Zd Zdd� Zdd� ZdS )�downloadc             C   s   || _ d|dd � i| _d S )NZhttps�   )�_l�_p)r   Z_linkr   r	   r	   r
   r   i   s    zdownload.__init__c       
   
   C   sf  d� t�tjt�d���}t|� d�d���0}tj| j	| j
dd�}|jdkrdtd|j� �� td	� td
|j� �� |j�d�}t|�td� }tdt|�� d�� d}|d kr�td� td� |�|j� n�x�|�d�D ]z}|t|�7 }|�|� td| �t|� }td| t|� d�}	tj�ddt|� ddt|�  |	df � tj��  q�W W d Q R X d S )N� �
   z.mp4�wbT)Zproxies�stream��   z!Failed
Status : r   z!Downloading...
Status : zContent-Lengthi   zSize : z mbr   z!Cant Get Content-Lengthz!Downloading... Please Waiti   �2   g      Y@r   z [%s%s] %s%s �+�.�%)�join�randomZsample�stringZascii_lowercaseZ	randrange�open�requests�getr8   r9   Zstatus_code�print�exitZheaders�int�float�writer   Ziter_contentr   �round�sys�stdout�flush)
r   Z	name_file�f�rZtotal�sizeZ_xr   ZdoneZprcnr	   r	   r
   �	_downloadm   s6    


zdownload._downloadN)r(   r)   r*   r   rU   r	   r	   r	   r
   r6   h   s   r6   z	
Title : �
zDownload?[y/n] �y)%r   rD   rE   rG   rO   r   r%   �	ExceptionrI   r   r   r   r2   �input�name�KeyboardInterruptrJ   Z_query�_proxy�
startswithr   r+   r   r1   Znew_event_loopr-   Zset_event_loopr0   r4   �objectr6   r   r   r!   �lowerZaskrU   r	   r	   r	   r
   �<module>   sT   (
 

$

