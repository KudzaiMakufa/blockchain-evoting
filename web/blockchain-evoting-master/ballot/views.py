import time, datetime
import uuid
from Crypto.Signature import DSS
from Crypto.Hash import SHA3_256
from Crypto.PublicKey import ECC
from Crypto import Random
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from ballot.models import Candidate
from ballot.forms import CandidateForm
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, TemplateView,
                                  UpdateView )

def create(request):
    candidates = None
    if request.method == 'POST':
        voter_id = request.POST.get('voter-id-input')
        vote = request.POST.get('vote-input')
        private_key = request.POST.get('private-key-input')

        # Create ballot as string vector
        timestamp = datetime.datetime.now().timestamp()
        ballot = "{}|{}|{}".format(voter_id, vote, timestamp)
        print('\ncasted ballot: {}\n'.format(ballot))
        signature = ''
        try:
            # Create signature
            priv_key = ECC.import_key(private_key)
            h = SHA3_256.new(ballot.encode('utf-8'))
            signature = DSS.new(priv_key, 'fips-186-3').sign(h)
            print('\nsignature: {}\n'.format(signature.hex()))

            # Verify the signature using registered public key
            pub_key = ECC.import_key(settings.PUBLIC_KEY)
            verifier = DSS.new(pub_key, 'fips-186-3')
        
            verifier.verify(h, signature)
            status = 'The ballot is signed successfully.'
            error = False
        except (ValueError, TypeError):
            status = 'The key is not registered.'
            error = True
        
        context = {
            'ballot': ballot,
            'signature': signature,
            'status': status,
            'error': error,
        }

        return render(request, 'ballot/status.html', context)
    else:
        candidates = Candidate.objects.filter()[:3]

        for item in candidates:
            print(item.photo.path)
    context = {
        'voter_id': uuid.uuid4(), 
        'candidates':candidates,
        }
    return render(request, 'ballot/create.html', context)

def delete_candidate(request):

    Candidate.objects.all().delete()
    messages.add_message(request, messages.INFO, ' Candidates removed')
    return render(request, 'ballot/create.html', {})


def seal(request):
    if request.method == 'POST':
        ballot = request.POST.get('ballot_input')
        ballot_byte = ballot.encode('utf-8')
        ballot_hash = SHA3_256.new(ballot_byte).hexdigest()
        # Puzzle requirement: '0' * n (n leading zeros)
        puzzle, pcount = settings.PUZZLE, settings.PLENGTH
        nonce = 0

        # Try to solve puzzle
        start_time = time.time() # benchmark
        timestamp = datetime.datetime.now().timestamp() # mark the start of mining effort
        while True:
            block_hash = SHA3_256.new(("{}{}{}".format(ballot, nonce, timestamp).encode('utf-8'))).hexdigest()
            print('\ntrial hash: {}\n'.format(block_hash))
            if block_hash[:pcount] == puzzle:
                stop_time = time.time() # benchmark
                print("\nblock is sealed in {} seconds\n".format(stop_time-start_time))
                break
            nonce += 1

        context = {
            'prev_hash': 'GENESIS',
            'transaction_hash': ballot_hash,
            'nonce': nonce,
            'block_hash': block_hash,
            'timestamp': timestamp,
        }
        return render(request, 'ballot/seal.html', context)
    return redirect('ballot:create')




class CreateCandidate(CreateView):
    model = Candidate
    template_name = 'ballot/create_candidate.html'
    form_class = CandidateForm

    def form_valid(self, form): 
        data = form.save(commit=False)
        data.created_at = timezone.now()
        data.updated_at = timezone.now()
        data.save()

        messages.add_message(self.request, messages.INFO, ' Candidate  successfully saved')
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse('ballot:create_candidate', kwargs={})

    def get_context_data(self, **kwargs):
            context = super(CreateCandidate, self).get_context_data(**kwargs)
            context['title'] = "Adding  Candidate"
            return context