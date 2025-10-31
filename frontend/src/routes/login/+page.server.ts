import type { PageServerLoad, Actions } from './$types';
import { redirect, fail } from '@sveltejs/kit';
import { fetchPOSTRequest } from '$lib/api/common';
// import { loginUser } from '$lib/user.model';

// export const load: PageServerLoad = (event) => {
//   const user = event.locals.user;

//   if (user) {
//     throw redirect(302, '/guarded');
//   }
// };

export const actions: Actions = {
  default: async ({ request, cookies }) => {
    // const formData = Object.fromEntries(await event.request.formData());
    const formData = await request.formData();
    const username = formData.get('username');
    const password = formData.get('password');

    if (!username || !password) {
      return fail(400, {
        error: 'Missing username or password'
      });
    }

    // const { username, password } = formData as { username: string; password: string };

    const response = await fetchPOSTRequest('/login', {
        username,
        password
    })

    const token = response.access_token;

    // return response

    // const { error, token } = await loginUser(email, password);

    // if (error) {
    //   return fail(401, {
    //     error
    //   });
    // }

    // Set the cookie
    
    cookies.set('access_token', `${token}`, {
      httpOnly: true,
      path: '/',
      secure: false,
      sameSite: 'strict',
      maxAge: 60 * 60 * 24 // 1 day
    });

    // throw redirect(302, '/guarded');
  }
};