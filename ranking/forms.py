from atento.ranking.models import *
from django.forms import *
 
class RankingForm(ModelForm):
    class Meta:
    model = Ranking

