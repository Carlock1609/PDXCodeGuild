USER AUTH
 user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password'],
            )
        if user is not None:
            login(request, user)
            return redirect('home')
